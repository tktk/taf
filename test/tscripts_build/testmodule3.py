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

module.TARGET = 'testmodule3'

module.SOURCE = {
    'testmodule3' : [
        'src1.cpp',
        'src2.cpp',
    ],
}
