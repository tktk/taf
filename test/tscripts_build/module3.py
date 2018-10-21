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

module.TARGET = 'module3'

module.SOURCE = {
    'module3' : [
        'src1.cpp',
        'src2.cpp',
    ],
}
