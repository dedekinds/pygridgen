`pygridgen`
===========
.. image:: https://travis-ci.org/phobson/pygridgen.svg?branch=develop
    :target: https://travis-ci.org/phobson/pygridgen
.. image:: https://coveralls.io/repos/phobson/pygridgen/badge.svg?branch=develop&service=github
  :target: https://coveralls.io/github/phobson/pygridgen?branch=develop


A Python interface to Pavel Sakov's `gridgen`_ library

.. _gridgen: https://github.com/sakov/gridgen-c

The full documentation for this for library is `here`_.

.. _here: https://phobson.github.io/pygridgen

For more detailed documentation on grid generation, manipulation, and visualization,
see the documentation for `pygridtools`_.

.. _pygridtools: https://phobson.github.io/pygridtools


Install
-------
cd pygridgen


cd external/nn; ./configure ;sudo make install


cd external/csa; ./configure ;sudo make install


cd external/gridutils; ./configure ;sudo make install


cd ..


cd gridgen; ./configure ;sudo make shlib


cd ..


cd ..


python setup.py install



Credits
-------
This fork of ``pygridgen`` stands on the very tall shoulders of `Robert Hetland`_ of Texas A&M University.
Many thanks to him, `Richard Signell`_, `Fillipe Fernandes`_, and all of the other contributors.

.. _Robert Hetland: https://github.com/hetland
.. _Richard Signell: https://github.com/rsignell-usgs
.. _Fillipe Fernandes: https://github.com/ocefpaf


Python Dependencies
-------------------

Basics
~~~~~~

Provided that all of the shared C libraries are installed, the remaining python depedencies are the following:

* numpy
* matplotlib
* pyproj (only if working with geographic coordinates)

Testing
~~~~~~~
```python
x = [0, 1, 2, 1, 0]
y = [0, 0, 1, 2, 2]
beta = [1, 1, 0, 1, 1]

focus = pygridgen.grid.Focus()
focus.add_focus_x(xo=0.5, factor=3, Rx=0.2)
focus.add_focus_y(yo=0.75, factor=5, Ry=0.1)
grid = pygridgen.grid.Gridgen(x, y, beta, shape=(20, 20), focus=focus)

fig, ax = plt.subplots()
ax.plot(x, y, 'k-')
ax.plot(grid.x, grid.y, 'b.')
plt.show()
```
