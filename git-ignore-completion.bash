#!/bin/bash

_git_ignore () {
	local subcommands="list print write"
	local subcommand="$(__git_find_on_cmdline "$subcommands")"

	if [ -z "$subcommand" ]; then
		__gitcomp "$subcommands"
		return
	fi

	case "$subcommand" in
	print)
		__git_ignore_print
		return
		;;
	write)
		__git_ignore_write
		return
		;;
	*)
		COMPREPLY=()
		;;
	esac
}

__git_ignore_save_templates() {
    curl http://gitignore.io/api/list 2>/dev/null | sed "s/,/ /g" | sort > ~/.git-ignore-templates
}

__git_ignore_templates() {
    if [ -f ~/.git-ignore-templates ]; then
        mtime=$(stat -f %m ~/.git-ignore-templates)
        now=$(date +%s)
        if (((${now} - ${mtime}) > 604800)); then
            __git_ignore_save_templates
        fi
    else
        __git_ignore_save_templates
    fi

    cat ~/.git-ignore-templates
}

__git_ignore_print() {
    templates=$(__git_ignore_templates)
    __gitcomp "$templates"
}

__git_ignore_write() {
    templates=$(__git_ignore_templates)
    __gitcomp "--overwrite $templates"
}

# alias __git_find_on_cmdline for backwards compatibility
if [ -z "`type -t __git_find_on_cmdline`" ]; then
	alias __git_find_on_cmdline=__git_find_subcommand
fi