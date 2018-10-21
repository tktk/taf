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
        features = 'dummyfeature',
        targetDir = _targetDir,
        targetName = _targetName,
        source = _source,
        lib = _lib,
        use = _use,
        userData = _userData,
    )

module.BUILDER = _build

module.TARGET = 'modulewithuserdata'

module.SOURCE = 'src.cpp'

module.LIB = 'lib'

module.USE = 'use'

module.USER_DATA = {
    'USER_DATA' : [
        'data1',
        'data2',
    ],
}
