# -*- coding: utf-8 -*-

TARGET = 'module3'

from . import module2

from taf import *

module.initialize()

module.DEPENDS = [
    module2.TARGET,
]

module.BUILDER = 'builder'

module.TARGET = TARGET

module.SOURCE = {
    'module3' : [
        'src1.cpp',
        'src2.cpp',
    ],
}

module.LIB = [
    'module3lib1',
    'module3lib2',
]
