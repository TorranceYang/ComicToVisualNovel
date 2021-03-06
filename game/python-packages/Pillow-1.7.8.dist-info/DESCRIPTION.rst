.. contents::

Pillow
======

Pillow is the "friendly" PIL fork. PIL is the Python Imaging Library. Pillow was
started for and is currently maintained by the Plone community. But it is used by
many other folks in the Python web community, and probably elsewhere too.

Introduction
------------

The fork author's goal is to foster packaging improvements via:

- Publicized development and solicitation of community support.
- Exploration of packaging problems within the fork, most noticably
  via adding setuptools support but also via clean up & refactoring
  of packaging code.

Why a fork?
-----------

PIL is currently not setuptools compatible. Please see
http://mail.python.org/pipermail/image-sig/2010-August/006480.html for a
more detailed explanation. Also, PIL's current release/maintenance schedule
is not compatible with the various & frequent packaging issues that have
occured.

What about image code bugs?
---------------------------

Please report any non-packaging related issues here first:

- https://bitbucket.org/effbot/pil-2009-raclette/issues 

Then open a ticket here:

- https://github.com/python-imaging/Pillow/issues

and provide a link to the first ticket so we can track the issue(s) upstream.
This project does not aim to fix image code bugs, but if we can track them
properly we may consider it. (And the image code could potentially be wholesale
replaced when the next PIL release comes out.)

Documentation
-------------

The API documentation included with PIL has been converted (from HTML) to
reStructured text (via pandoc) and is now `hosted by readthedocs.org`_.

.. _`hosted by readthedocs.org`: http://pillow.readthedocs.org

What follows is the original PIL README.

Python Imaging Library
======================

Introduction
------------

The Python Imaging Library (PIL) adds image processing capabilities
to your Python environment.  This library provides extensive file
format support, an efficient internal representation, and powerful
image processing capabilities.

This source kit has been built and tested with Python 2.0 and newer,
on Windows, Mac OS X, and major Unix platforms.  Large parts of the
library also work on 1.5.2 and 1.6.

The main distribution site for this software is:

        http://www.pythonware.com/products/pil/

That site also contains information about free and commercial support
options, PIL add-ons, answers to frequently asked questions, and more.

Development versions (alphas, betas) are available here:

        http://effbot.org/downloads/

The PIL handbook is not included in this distribution; to get the
latest version, check:

        http://www.pythonware.com/library/

For installation and licensing details, see below.

--------------------------------------------------------------------
Support Options
--------------------------------------------------------------------

Commercial Support
~~~~~~~~~~~~~~~~~~

Secret Labs (PythonWare) offers support contracts for companies using
the Python Imaging Library in commercial applications, and in mission-
critical environments.  The support contract includes technical support,
bug fixes, extensions to the PIL library, sample applications, and more.

For the full story, check:

        http://www.pythonware.com/products/pil/support.htm


Free Support
~~~~~~~~~~~~

For support and general questions on the Python Imaging Library, send
e-mail to the Image SIG mailing list:

        image-sig@python.org

You can join the Image SIG by sending a mail to:

        image-sig-request@python.org

Put "subscribe" in the message body to automatically subscribe to the
list, or "help" to get additional information.  Alternatively, you can
send your questions to the Python mailing list, python-list@python.org,
or post them to the newsgroup comp.lang.python.  DO NOT SEND SUPPORT
QUESTIONS TO PYTHONWARE ADDRESSES.


--------------------------------------------------------------------
Software License
--------------------------------------------------------------------

The Python Imaging Library is

Copyright (c) 1997-2009 by Secret Labs AB
Copyright (c) 1995-2009 by Fredrik Lundh

By obtaining, using, and/or copying this software and/or its
associated documentation, you agree that you have read, understood,
and will comply with the following terms and conditions:

Permission to use, copy, modify, and distribute this software and its
associated documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appears in all
copies, and that both that copyright notice and this permission notice
appear in supporting documentation, and that the name of Secret Labs
AB or the author not be used in advertising or publicity pertaining to
distribution of the software without specific, written prior
permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR
ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

--------------------------------------------------------------------
Build instructions (all platforms)
--------------------------------------------------------------------

For a list of changes in this release, see the CHANGES document.

0. If you're in a hurry, try this::

        $ tar xvfz Imaging-1.1.7.tar.gz
        $ cd Imaging-1.1.7
        $ python setup.py install

   If you prefer to know what you're doing, read on.


1. Prerequisites.

   If you need any of the features described below, make sure you
   have the necessary libraries before building PIL.

   +----------------------+---------------------------------------------+
   |  feature             |library                                      |
   +----------------------+---------------------------------------------+
   |  JPEG support        |libjpeg (6a or 6b)                           |
   |                      |                                             |           
   |                      |http://www.ijg.org                           |
   |                      |http://www.ijg.org/files/jpegsrc.v6b.tar.gz  |
   |                      |ftp://ftp.uu.net/graphics/jpeg/              |
   +----------------------+---------------------------------------------+
   |                      |                                             |           
   |  PNG support         |zlib (1.2.3 or later is recommended)         |
   |                      |                                             |           
   |                      |http://www.gzip.org/zlib/                    |
   +----------------------+---------------------------------------------+
   |                      |                                             |           
   |  OpenType/TrueType   |freetype2 (2.3.9 or later is recommended)    |
   |  support             |                                             |
   |                      |http://www.freetype.org                      |
   |                      |http://freetype.sourceforge.net              |
   +----------------------+---------------------------------------------+
   |                      |                                             |           
   |  CMS support         |littleCMS (1.1.5 or later is recommended)    |
   |                      |http://www.littlecms.com/                    |
   +----------------------+---------------------------------------------+

   If you have a recent Linux version, the libraries provided with the
   operating system usually work just fine.  If some library is
   missing, installing a prebuilt version (jpeg-devel, zlib-devel,
   etc) is usually easier than building from source.  For example, for
   Ubuntu 9.10 (karmic), you can install the following libraries::

       sudo apt-get install libjpeg62-dev
       sudo apt-get install zlib1g-dev
       sudo apt-get install libfreetype6-dev
       sudo apt-get install liblcms1-dev

   If you're using Mac OS X, you can use the 'fink' tool to install
   missing libraries (also see the Mac OS X section below).

   Similar tools are available for many other platforms.


2. To build under Python 1.5.2, you need to install the stand-alone
   version of the distutils library:

       http://www.python.org/sigs/distutils-sig/download.html

   You can fetch distutils 1.0.2 from the Python source repository:

       svn export http://svn.python.org/projects/python/tags/Distutils-1_0_2/Lib/distutils/

   For newer releases, the distutils library is included in the
   Python standard library.

   NOTE: Version 1.1.7 is not fully compatible with 1.5.2.  Some
   more recent additions to the library may not work, but the core
   functionality is available.


3. If you didn't build Python from sources, make sure you have
   Python's build support files on your machine.  If you've down-
   loaded a prebuilt package (e.g. a Linux RPM), you probably
   need additional developer packages.  Look for packages named
   "python-dev", "python-devel", or similar.  For example, for
   Ubuntu 9.10 (karmic), use the following command:

       sudo apt-get install python-dev


4. When you have everything you need, unpack the PIL distribution
   (the file Imaging-1.1.7.tar.gz) in a suitable work directory::

        $ cd MyExtensions # example
        $ gunzip Imaging-1.1.7.tar.gz
        $ tar xvf Imaging-1.1.7.tar


5. Build the library.  We recommend that you do an in-place build,
   and run the self test before installing::

        $ cd Imaging-1.1.7
        $ python setup.py build_ext -i
        $ python selftest.py

   During the build process, the setup.py will display a summary
   report that lists what external components it found.  The self-
   test will display a similar report, with what external components
   the tests found in the actual build files::

        --------------------------------------------------------------------
        Pillow 1.5 ( PIL fork based on PIL 1.1.7 ) SETUP SUMMARY
        --------------------------------------------------------------------
        platform  darwin 2.6.6 (r266:84292, Nov 26 2010, 16:24:16)
          [GCC 4.2.1 (Apple Inc. build 5664)]
        --------------------------------------------------------------------
        --- TKINTER support available
        --- JPEG support available
        --- ZLIB (PNG/ZIP) support available
        *** FREETYPE2 support not available
        *** LITTLECMS support not available
        --------------------------------------------------------------------

   Make sure that the optional components you need are included.

   If the build script won't find a given component, you can edit the
   setup.py file and set the appropriate ROOT variable.  For details,
   see instructions in the file.

   If the build script finds the component, but the tests cannot
   identify it, try rebuilding *all* modules::

        $ python setup.py clean
        $ python setup.py build_ext -i


6. If the setup.py and selftest.py commands finish without any
   errors, you're ready to install the library::

        $ python setup.py install

   (depending on how Python has been installed on your machine,
   you might have to log in as a superuser to run the 'install'
   command, or use the 'sudo' command to run 'install'.)


Additional notes for Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Mac OS X you will usually install additional software such as
libjpeg or freetype with the "fink" tool, and then it ends up in
"/sw".  If you have installed the libraries elsewhere, you may have
to tweak the "setup.py" file before building.


Additional notes for Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Windows, you need to tweak the ROOT settings in the "setup.py"
file, to make it find the external libraries.  See comments in the
file for details.

Make sure to build PIL and the external libraries with the same
runtime linking options as was used for the Python interpreter
(usually /MD, under Visual Studio).


Note that most Python distributions for Windows include libraries
compiled for Microsoft Visual Studio.  You can get the free Express
edition of Visual Studio from:

    http://www.microsoft.com/Express/

To build extensions using other tool chains, see the "Using
non-Microsoft compilers on Windows" section in the distutils handbook:

    http://www.python.org/doc/current/inst/non-ms-compilers.html

For additional information on how to build extensions using the
popular MinGW compiler, see:

    http://mingw.org (compiler)
    http://sebsauvage.net/python/mingw.html (build instructions)
    http://sourceforge.net/projects/gnuwin32 (prebuilt libraries)


Changelog
=========

1.7.8 (2012-11-01)
------------------

- Removed doctests.py that made tests of other packages fail.
  [thomasdesvenain]

- Fix opening psd files with RGBA layers when A mode is not of type 65535 but 3.
  Fixes issue https://github.com/python-imaging/Pillow/issues/3
  [thomasdesvenain]


1.7.7 (2012-04-04)
------------------

- UNDEF more types before including windows headers
  [mattip]

1.7.6 (2012-01-20)
------------------

- Bug fix: freetype not found on Mac OS X with case-sensitive filesystem
  [gjo]

- Bug fix: Backport fix to split() after open() (regression introduced in PIL 1.1.7).
  [sfllaw]

1.7.5 (2011-09-07)
------------------

- Fix for sys.platform = "linux3"
  [blueyed]

- Package cleanup and additional documentation
  [aclark]

1.7.4 (2011-07-21)
------------------

- Fix brown bag release
  [aclark]

1.7.3 (2011-07-20)
------------------

- Fix : resize need int values, append int conversion in thumbnail method
  [harobed]

1.7.2 (2011-06-02)
------------------

- Bug fix: Python 2.4 compat
  [aclark]

1.7.1 (2011-05-31)
------------------

- More multi-arch support
  [SteveM, regebro, barry, aclark]

1.7.0 (2011-05-27)
------------------

- Add support for multi-arch library directory /usr/lib/x86_64-linux-gnu
  [aclark]

1.6 (12/01/2010)
----------------

- Bug fix: /usr/x11/include should be added to include_dirs not library_dirs
  [elro]

- Doc fixes

1.5 (11/28/2010)
----------------

- Module and package fixes

1.4 (11/28/2010)
----------------

- Doc fixes

1.3 (11/28/2010)
----------------

- Add support for /lib64 and /usr/lib64 library directories on Linux
- Doc fixes

1.2 (08/02/2010)
----------------

- On OS X also check for freetype2 in the X11 path [jezdez]
- Doc fixes [aclark]

1.1 (07/31/2010)
----------------

- Removed setuptools_hg requirement
- Doc fixes

1.0 (07/30/2010)
----------------

- Forked PIL based on Hanno Schlichting's re-packaging
  (http://dist.plone.org/thirdparty/PIL-1.1.7.tar.gz)


