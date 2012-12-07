# whichpkg
## Locate the path of a specific python module
If you're at all like me, you're always needing to open up and look at the source code of installed packages and it required more process than I liked to just determine their path.

### Installation
`$ pip install whichpkg`

### Usage
```
$ whichpkg simplejson
/Users/matt/.virtualenvs/whichpkg/lib/python2.7/site-packages/simplejson
$ whichpkg django gevent
/Users/matt/.virtualenvs/whichpkg/lib/python2.7/site-packages/django
/Users/matt/.virtualenvs/whichpkg/lib/python2.7/site-packages/gevent
$ whichpkg doesnotexist
doesnotexist not found
```
```
Usage: whichpkg package [package]
```
