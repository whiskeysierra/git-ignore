# ![Block icon](icon.png) git-ignore [![Build Status](https://travis-ci.org/whiskeysierra/git-ignore.png?branch=master,develop)](http://travis-ci.org/whiskeysierra/git-ignore)

`git-ignore` is small custom git command which helps you generate a `.gitignore` file based on your needs.

This script is based on [gitignore.io](http://gitignore.io/)'s api.

![gitignore.io logo](https://raw.github.com/joeblau/gitignore.io/master/public/gi/img/gitignore-logo-dark.png)

If you think a template is incomplete or missing, please contribute back to 
[joeblau/gitignore.io](https://github.com/joeblau/gitignore.io) and/or 
[github/gitignore](https://github.com/github/gitignore)

## Requirements

- Python 2.6 or 2.7

To install the required python libraries run:
    
    sudo pip install -r requirements.txt

## Quickstart

Just put add ´git-ignore´ to you `PATH` and use it like any other `git` command.

Before the first run, you need to update your local repository of known templates, which is located at `~/.gitignore`, by
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

What basically happend: for [every known template of gitignore.io](http://gitignore.io/api/list) we saved a corresponding
`.gitignore` template file to `.gitignore/<template>`. This way you only have to update your local template repository
once in a while and don't need an internet connection.

A new `.gitignore` file can be generated like this:

    git ignore write intellij python

If you want to overwrite an existing file specify the `--overwrite` switch:

    git ignore write --overwrite intellij python

For debug purposes, you can just print the output to stdout:

    git ignore print intellij python

A list of all locally available templates can be viewed with:

    git ignore ignore list

For more detailed information use

    git ignore --help

## Attributions
![Creative Commons License](http://i.creativecommons.org/l/by-nd/3.0/80x15.png)
Block Icon by [Visual Pharm](http://www.iconfinder.com/icondetails/27836/128/approve_block_cancel_delete_reject_icon) is licensed under a
[Creative Commons (Attribution-NoDerivs 3.0 Unported)](http://creativecommons.org/licenses/by-nd/3.0/).



