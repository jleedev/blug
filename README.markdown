Blug readme
===========

Blug is a tiny blog engine that uses [Django][], [Markdown][], and
[Smartypants][] (actually [smartypants.py][]). It was inspired by Tom
Preston-Werner's [Jekyll][], except it is written in Python instead of
Ruby and runs as a web application instead of offline. What can I say, I needed something to do.

[django]:           http://www.djangoproject.com/
[markdown]:         http://daringfireball.net/projects/markdown/
[smartypants]:      http://daringfireball.net/projects/smartypants/
[jekyll]:           http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html
[smartypants.py]:   http://web.chad.org/projects/smartypants.py/

Blug doesn't do anything fancy like layouts, templates, or related
posts; but that's because it was written in an hour. There's just a flat
list of posts, and they all get formatted and rendered against the same
Django template. There's no web interface for posting, either; just a
directory on the filesystem containing the properly-named entries.

Notes
-----

* `python-django` and `python-markdown` are in Debian/Ubuntu.
* Install smartypants.py with `easy_install smartypants`.
* The repository needs to be a directory called `mysite`, due to `settings.py`.

Once everything is set up, just run `./manage.py runserver` and go to
http://localhost:8000/blug/ to see it in action.
