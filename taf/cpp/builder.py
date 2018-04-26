# -*- coding: utf-8 -*-

from . import *
from .. import builder
from .. import taf

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
        _LIB + [ 'gtest' ],
        _USE,
    )

def _build(
    _FEATURES,
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    _context(
        features = _FEATURES,
        target = _TARGET,
        source = builder.generateSource(
            _SOURCE,
            os.path.join(
                getSourceDir(),
                taf.PACKAGE_NAME,
            ),
            '.cpp',
        ),
        lib = _LIB,
        use = _USE,
    )
