test-widget
===========

This is a small test project to demonstrate the functionality of a web widget
loaded via an Iframe, that can be interacted with from the parent window by
[message passing](https://developer.mozilla.org/en-US/docs/Web/API/Window.postMessage).

The Iframe loads a set of images tagged with 'starting' and accepts the name
of a tag to load a different set of images. These can be added via the Django
admin.


Usage
-----

Insert the following script tag into your page _at the bottom_ of the `body` tag:

```
<script src="http://host/static/widget.js"></script>
```
... where `host` is the server where the app is deployed.

Anywhere _above_ that script tag, insert the following:

```
<a id="widget" href="http://host"></a>
```

This anchor tag will be replaced by the Iframe when the `widget.js` script is
loaded.

In order to change the images displayed in the widget, you can send it the name
of the tag to load, like so:

```
<script>
    var iframe = document.getElementById('widget').contentWindow,
        button = document.getElementById('load-tag'),
        tag = document.getElementById('tag');

    button.onclick = function() {
      iframe.postMessage({tag: tag.value}, 'http://host');
    }
</script>
```

See a working example (if the server is up)
[here](http://imiric.github.io/test-widget/).


Development
-----------

1. Install the latest version of [Docker](https://www.docker.com/).

2. Run a PostgreSQL container:

        docker run -d --name postgres postgres:9.3

3. Create the database:

        docker run --rm --link postgres:db postgres:9.3 psql -h db -U postgres -c 'CREATE DATABASE widget;'  

4. Clone this repo and create the `widget` image:

        docker build -t widget . 

5. Run Django migrations:

        docker run --rm --link postgres:db -v $(pwd):/usr/src/app widget ./manage.py migrate

6. Optionally create the Django admin user:

        docker run -it --rm --link postgres:db -v $(pwd):/usr/src/app widget ./manage.py createsuperuser

7. Run the app:

        docker run -it --rm --link postgres:db -p 8000:8000 -v $(pwd):/usr/src/app widget ./manage.py runserver 0.0.0.0:8000

To run the tests:

    docker run --rm --link postgres:db -v $(pwd):/usr/src/app widget ./manage.py test


License
-------

[MIT](LICENSE)
