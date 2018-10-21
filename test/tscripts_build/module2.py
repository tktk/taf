# -*- coding: utf-8 -*-

from taf import *

def _build(
    _context,
    _targetDir,
    _targetName,
    _source,
    _lib,
    _use,
    _userData,
):
    _context(
        features = [
            'dummyfeature1',
            'dummyfeature2',
        ],
        targetDir = _targetDir,
        targetName = _targetName,
        source = _source,
        lib = _lib,
        use = _use,
    )

module.BUILDER = _build

module.TARGET = 'module2'

module.SOURCE = {
    'module2' : {
        'c' : [
            'src2.cpp',
            'src1.cpp',
        ],
        'b' : [
            'src2.cpp',
            'src1.cpp',
        ],
        'a' : [
            'src2.cpp',
            'src1.cpp',
        ],
    },
}

module.LIB = [
    'module2lib1',
    'module2lib2',
]

module.USE = [
    'module2use1',
    'module2use2',
]
