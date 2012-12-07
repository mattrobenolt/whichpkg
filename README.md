# whichpkg
## Locate the path of a specific python module
Should work exactly like `which`.

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
