Electrum-POLIS - Lightweight Polis client
=====================================

::

  Licence: MIT Licence
  Author: Thomas Voegtlin
  Language: Python
  Homepage: https://electrum-polis.org/


.. image:: https://travis-ci.org/akhavr/electrum-polis.svg?branch=develop
    :target: https://travis-ci.org/akhavr/electrum-polis
    :alt: Build Status
.. image:: https://coveralls.io/repos/github/spesmilo/electrum/badge.svg?branch=master
    :target: https://coveralls.io/github/spesmilo/electrum?branch=master
    :alt: Test coverage statistics
.. image:: https://img.shields.io/badge/help-translating-blue.svg
    :target: https://crowdin.com/project/electrum
    :alt: Help translating Electrum online





Getting started
===============

<<<<<<< HEAD
Electrum-POLIS is a pure python application. If you want to use the
=======
Electrum is a pure python application. If you want to use the
>>>>>>> bitcoinElectrum/master
Qt interface, install the Qt dependencies::

    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
<<<<<<< HEAD
Electrum-POLIS from its root directory, without installing it on your
=======
Electrum from its root directory, without installing it on your
>>>>>>> bitcoinElectrum/master
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-POLIS from its root directory, just do::

    ./electrum-polis

<<<<<<< HEAD
You can also install Electrum-POLIS on your system, by running this command::

    python setup.py install

This will download and install the Python dependencies used by
Electrum-POLIS, instead of using the 'packages' directory.

If you cloned the git repository, you need to compile extra files
before you can run Electrum-POLIS. Read the next section, "Development
=======
You can also install Electrum on your system, by running this command::

    sudo apt-get install python3-setuptools
    pip3 install .[full]

This will download and install the Python dependencies used by
Electrum, instead of using the 'packages' directory.
The 'full' extra contains some optional dependencies that we think
are often useful but they are not strictly needed.

If you cloned the git repository, you need to compile extra files
before you can run Electrum. Read the next section, "Development
>>>>>>> bitcoinElectrum/master
Version".



Development version
===================

Check out the code from GitHub::

    git clone https://github.com/akhavr/electrum-polis
    cd electrum-polis

Run install (this should install dependencies)::

    pip3 install .[full]

Compile the icons file for Qt::

    sudo apt-get install pyqt5-dev-tools
    pyrcc5 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations (optional)::

    sudo apt-get install python-requests gettext
    ./contrib/make_locale




Creating Binaries
=================


To create binaries, create the 'packages' directory::

    ./contrib/make_packages

This directory contains the python dependencies used by Electrum.

Mac OS X / macOS
--------

<<<<<<< HEAD
::

    # On MacPorts installs:
    sudo python setup-release.py py2app

    # On Homebrew installs:
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

    sudo hdiutil create -fs HFS+ -volname "Electrum" -srcfolder dist/Electrum.app dist/electrum-VERSION-macosx.dmg
=======
See `contrib/build-osx/`.
>>>>>>> bitcoinElectrum/master

Windows
-------

<<<<<<< HEAD
See `contrib/build-wine/README` file.
=======
See `contrib/build-wine/`.
>>>>>>> bitcoinElectrum/master


Android
-------

See `gui/kivy/Readme.txt` file.
