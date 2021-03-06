from pkg_resources import resource_filename

import pytest

import pygridgen

def test(*args):
    options = [resource_filename('pygridgen', 'tests')]
    options.extend(list(args))
    return pytest.main(options)
