# -*- coding: utf-8 -*-

from taf import *

module.DEPENDS = [
    'depend1',
]

module.BUILDER = 'builder'

module.TARGET = 'module1'

module.SOURCE = {
    'module1' : [
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
