===========
ADAS Viewer
===========

ADAS Viewer is a Django app to provide Web-based GUI of ADAS. For each dataset,
visitors can also filter the datasets based on the standard parameter name in
addition to the basic filtering of geospaas basic Viewer. The documentation of
geospaas basic viewer for basic filtering is provided
in description section of https://github.com/nansencenter/django-geo-spaas/blob/master/geospaas/base_viewer.

Usage
-----
`Parameter standard name` is searchable by

the ``full Parameter standard name``

`or`

``a part of it.``



Quick start for developers
--------------------------

1. Having the geospaas in your machine, clone this repo and add "geospaas_adas_viewer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'geospaas_adas_viewer',
    ]

2. open your browser with `localhost:8080/adas/` after running the runserver command of django
