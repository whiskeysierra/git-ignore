#!/usr/bin/env python

from __future__ import print_function, unicode_literals

import argparse
import os
import requests
import sys

from clint.textui import colored, puts


def parse():
    parser = argparse.ArgumentParser(description='Generates a .gitignore file using http://gitignore.io')

    commands = parser.add_subparsers(help='Available commands')

    list_command = commands.add_parser('list', help='List all available templates.')
    list_command.set_defaults(command='list')

    print_command = commands.add_parser('print', help='Print the ignore patterns of the specified templates.')
    print_command.set_defaults(command='print')
    print_command.add_argument('templates', nargs='+', metavar='template',
                               help='Selected templates used to generate the .gitignore patterns.')

    write_command = commands.add_parser('write', help='Writes the specified templates to the .gitignore file.')
    write_command.set_defaults(command='write')
    write_command.add_argument('--overwrite', dest='overwrite', action='store_true', default=False)
    write_command.add_argument('templates', nargs='+', metavar='template',
                               help='Selected templates used to generate the .gitignore file.')

    return parser.parse_args()

args = parse()


def list_templates():
    templates = sorted(requests.get('http://gitignore.io/api/list').text.strip().split(','))
    for template in templates:
        print(template)


def generate_content(templates):
    parts = []

    for template in templates:
        content = requests.get('http://gitignore.io/api/%s' % template).text
        # skip comment header
        lines = content.splitlines()

        if not lines[0] == '# Generated by http://gitignore.io':
            raise IOError('Invalid content: \n%s' % content)

        content = '\n'.join(lines[2:])

        parts.append(content)

    return '\n\n'.join(parts) + '\n'


def print_templates():
    puts(generate_content(args.templates), newline=False)


def write_templates():
    puts("Writing... ", newline=False)

    gitignore = os.path.join(os.getcwd(), '.gitignore')

    if not args.overwrite and os.path.exists(gitignore):
        print(colored.yellow('exists'))
    else:
        try:
            with open(gitignore, 'w') as f:
                f.write(generate_content(args.templates))
                print(colored.green('done'))
        except Exception:
            print(colored.red('failed'))

actions = {
    'list': list_templates,
    'print': print_templates,
    'write': write_templates,
}


def unknown():
    raise RuntimeError("Unknown command '%s'" % args.command)


def on_error(message):
    sys.stderr.write(str(message) + '\n')


# see http://www.freebsd.org/cgi/man.cgi?query=sysexits&sektion=3
try:
    action = actions.get(args.command, unknown)
    action()
except Exception, e:
    on_error(e)
    sys.exit(70)
