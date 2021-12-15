Install Guide
==============

Being a modern Python library, **PyTgCalls** requires Python 3.6+ to be installed in your system.
We recommend using the latest versions of both Python 3 and pip.

- Get **Python 3** from https://www.python.org/downloads/ (or with your package manager).
- Get **pip** by following the instructions at https://pip.pypa.io/en/latest/installing/.

.. important::

    PyTgCalls supports **Python 3** only, starting from version 3.6. **PyPy** is supported too.

-----

Install PyTgCalls
-----------------

-   The easiest way to install and upgrade PyTgCalls to its latest stable version is by using **pip**:

    .. code-block:: bash

        $ pip3 install -U py-tgcalls

Bleeding Edge
-------------

PyTgCalls is always evolving, although new releases on PyPI are published only when enough changes are added, but this
doesn't mean you can't try new features right now!

In case you'd like to try out the latest PyTgCalls features, the `GitHub repo`_ is always kept updated with new changes;
you can install the development version straight from the ``master`` branch using this command (note "master.zip" in
the link):

.. code-block:: bash

    $ pip3 install -U git+https://github.com/pytgcalls/pytgcalls

Verifying
---------

To verify that PyTgCalls is correctly installed, open a Python shell and import it.
If no error shows up you are good to go.

.. parsed-literal::

    >>> import pytgcalls
    >>> pytgcalls.__version__
    '|version|'

.. _`Github repo`: http://github.com/pyrogram/pyrogram
