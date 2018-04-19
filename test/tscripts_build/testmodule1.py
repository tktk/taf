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
            'dummyfeature1',
            'dummyfeature2',
        ],
        target = _target,
        source = _source,
        lib = _lib,
        use = _use,
    )

module.BUILDER = _build

module.TARGET = 'testmodule1'

module.SOURCE = {
    'testmodule1' : [
        'src1.cpp',
        'src2.cpp',
    ],
}

module.LIB = [
    'module1lib1',
    'module1lib2',
]

module.USE = [
    'module1use1',
    'module1use2',
]
