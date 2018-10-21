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
            'dummyfeature',
        ],
        targetDir = _targetDir,
        targetName = _targetName,
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
