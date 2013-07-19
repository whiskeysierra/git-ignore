# ![Block icon](icon.png) git-ignore [![Build Status](https://travis-ci.org/whiskeysierra/git-ignore.png?branch=master,develop)](http://travis-ci.org/whiskeysierra/git-ignore)

`git-ignore` is small custom git command which helps you generate a `.gitignore` file based on your needs.

![gitignore.io logo](http://gitignore.io/gi/img/gitignore-logo-light.png)

This script is based on the api of [gitignore.io](http://gitignore.io/)

## Requirements

- Python 2.6 or 2.7

To install the required python libraries run:
    
    sudo pip install -r requirements.txt

## Quickstart

Just put add ´git-ignore´ to you `PATH` and use it like any other `git` command.

Before the first run, you need to update your local repository of known tags, which is located at `~/.gitignore`, by
running:

    git ignore update

It should give you something like the following:

    Updating...
        actionscript... done
        android... done
        appceleratortitanium... done
        archives... done
        autotools... done
        bancha... done
        basercms... done
        c... done
        c++... done
        cakephp... done
        cfwheels... done
        clojure... done
        ...

What basically happend: for [every known tag of gitignore.io](http://gitignore.io/api/list) we saved corresponding
`.gitignore` file to `.gitignore/&lt;tag&gt;´

A new `.gitignore` file can be generated like this:

    git ignore write intellij python

If you want to overwrite an existing file specify the `--overwrite` switch:

    git ignore write intellij python

For debug purposes, you can just print the output to stdout:

    git ignore print intellij python

A list of all locally available tags can be viewed with:

    git ignore ignore list

For more detailed information use

    git ignore --help

## Attributions
![Creative Commons License](http://i.creativecommons.org/l/by-nd/3.0/80x15.png)
Block Icon by [Visual Pharm](http://www.iconfinder.com/icondetails/27836/128/approve_block_cancel_delete_reject_icon) is licensed under a
[Creative Commons (Attribution-NoDerivs 3.0 Unported)](http://creativecommons.org/licenses/by-nd/3.0/).



