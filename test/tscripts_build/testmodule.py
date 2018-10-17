# -*- coding: utf-8 -*-

from taf import *

def _build(
    _context,
    _target,
    _source,
    _lib,
    _use,
):
    _context(
        features = [
            'dummyfeature',
        ],
        target = _target,
        source = _source,
        lib = _lib,
        use = _use,
    )

module.BUILDER = _build

module.TYPE = module.test

module.TARGET = 'testmodule'

module.SOURCE = {
    'testmodule' : [
        'src.cpp',
    ],
}
