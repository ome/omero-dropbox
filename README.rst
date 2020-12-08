OMERO.dropbox
=============

.. image:: https://github.com/ome/omero-dropbox/workflows/OMERO/badge.svg
   :target: https://github.com/ome/omero-dropbox/actions
.. image:: https://github.com/ome/omero-dropbox/workflows/Tox/badge.svg
   :target: https://github.com/ome/omero-dropbox/actions
.. image:: https://github.com/ome/omero-dropbox/workflows/PyPI/badge.svg
   :target: https://github.com/ome/omero-dropbox/actions

Introduction
------------

OMERO.dropbox provides a server for watching directories
for new files which are then imported into OMERO.

Dependencies
------------

Direct dependencies of OMERO.dropbox are:

- `ZeroC IcePy`_
- `OMERO.py`_

Installation
------------

See: `OMERO`_ documentation

Usage
-----

See: `OMERO`_ documentation

Contributing
------------

See: `OMERO`_ documentation

Running tests
-------------

Unit tests are located under the `test` directory and can be run with pytest.

Integration tests
^^^^^^^^^^^^^^^^^

Integration tests are stored in the main repository (ome/openmicroscopy) and depend on the
OMERO integration testing framework. Reading about `Running and writing tests`_ in the `OMERO`_ documentation
is essential.

Release process
---------------

This repository uses `bump2version <https://pypi.org/project/bump2version/>`_ to manage version numbers.
To tag a release run::

    $ bumpversion release

This will remove the ``.dev0`` suffix from the current version, commit, and tag the release.

To switch back to a development version run::

    $ bumpversion --no-tag [major|minor|patch]

specifying ``major``, ``minor`` or ``patch`` depending on whether the development branch will be a `major, minor or patch release <https://semver.org/>`_. This will also add the ``.dev0`` suffix.

Remember to ``git push`` all commits and tags.

License
-------

OMERO.dropbox is released under the GPL v2.

Copyright
---------

2009-2020, The Open Microscopy Environment, Glencoe Software, Inc.

.. _OMERO: https://www.openmicroscopy.org/omero
.. _OMERO.py: https://pypi.python.org/pypi/omero-py
.. _ZeroC IcePy: https://zeroc.com/
.. _Running and writing tests: https://docs.openmicroscopy.org/latest/omero/developers/testing.html
