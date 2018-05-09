# -*- coding: utf-8 -*-

from . import *
from .. import builder
from ... import taf

import os.path

def program(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    _build(
        [
            'cxx',
            'cxxprogram',
        ],
        _context,
        _TARGET,
        _SOURCE,
        _LIB,
        _USE,
    )

def shlib(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    _build(
        [
            'cxx',
            'cxxshlib',
        ],
        _context,
        _TARGET,
        _SOURCE,
        _LIB,
        _USE,
    )

def gtest(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    _build(
        [
            'cxx',
            'cxxprogram',
            'test',
        ],
        _context,
        _TARGET,
        _SOURCE,
        _LIB,
        _USE,
        [ 'gtest' ],
        [ 'TEST' ],
    )

def _build(
    _FEATURES,
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
    _APPEND_LIB = [],
    _APPEND_USE = [],
):
    lib = []
    if _LIB is not None:
        lib.extend( _LIB )

    lib.extend( _APPEND_LIB )

    use = []
    if _USE is not None:
        use.extend( _USE )

    use.extend( _APPEND_USE )

    _context(
        features = _FEATURES,
        target = _TARGET,
        source = builder.generateSource(
            _SOURCE,
            os.path.join(
                getSourceDir(),
                taf.PACKAGE_NAME,
            ),
        ),
        lib = lib,
        use = use,
    )
