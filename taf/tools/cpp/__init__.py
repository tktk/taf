# -*- coding: utf-8 -*-

INCLUDES = None

SOURCE_DIR = 'src'
HEADER_DIR = 'inc'

CXXFLAGS_GCC_COMMON_DEFAULT = [
    '-Wall',
    '-fno-rtti',
    '-fvisibility=hidden',
    '-std=c++14',
]

CXXFLAGS_GCC_DEBUG_DEFAULT = [
    '-O0',
    '-g'
]

CXXFLAGS_GCC_RELEASE_DEFAULT = [
    '-O2',
]

CXXFLAGS_GCC_DEBUG = CXXFLAGS_GCC_COMMON_DEFAULT + CXXFLAGS_GCC_DEBUG_DEFAULT
CXXFLAGS_GCC_RELEASE = CXXFLAGS_GCC_COMMON_DEFAULT + CXXFLAGS_GCC_RELEASE_DEFAULT

def getIncludes(
):
    return INCLUDES

def getSourceDir(
):
    return SOURCE_DIR

def getHeaderDir(
):
    return HEADER_DIR

def getCxxflagsGccDebug(
):
    return CXXFLAGS_GCC_DEBUG

def getCxxflagsGccRelease(
):
    return CXXFLAGS_GCC_RELEASE

from .options import options
from .configure import configure

from .builder import *
