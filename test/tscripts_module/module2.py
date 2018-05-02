# -*- coding: utf-8 -*-

TARGET = 'module2'

from . import module3

from taf import *

module.initialize()

module.DEPENDS = [
    module3.TARGET,
]

module.BUILDER = 'builder'

module.TARGET = TARGET

module.SOURCE = {
    'module2' : [
        'src1.cpp',
        'src2.cpp',
    ],
}

module.LIB = [
    'module2lib1',
    'module2lib2',
]

module.USE = [
    'module2use1',
    'module2use2',
]
