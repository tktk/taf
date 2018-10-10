# -*- coding: utf-8 -*-

SOURCE_DIR = 'src'
HEADER_DIR = 'inc'

INCLUDES = None

CXXFLAGS_COMMON_DEFAULT = [
    '-Wall',
    '-fno-exceptions',
    '-fno-rtti',
    '-fvisibility=hidden',
    '-std=c++14',
]

CXXFLAGS_DEBUG_DEFAULT = [
    '-O0',
    '-g'
]

CXXFLAGS_RELEASE_DEFAULT = [
    '-O2',
    '-g0'
]

CXXFLAGS_DEBUG = CXXFLAGS_COMMON_DEFAULT + CXXFLAGS_DEBUG_DEFAULT
CXXFLAGS_RELEASE = CXXFLAGS_COMMON_DEFAULT + CXXFLAGS_RELEASE_DEFAULT

DEFINES_COMMON_DEFAULT = [
    '_PSP_FW_VERSION=150',
]

DEFINES_DEBUG_DEFAULT = [
    'DEBUG',
]

DEFINES_RELEASE_DEFAULT = [
]

DEFINES_DEBUG = DEFINES_COMMON_DEFAULT + DEFINES_DEBUG_DEFAULT
DEFINES_RELEASE = DEFINES_COMMON_DEFAULT + DEFINES_RELEASE_DEFAULT

LINKFLAGS_COMMON_DEFAULT = [
]

LINKFLAGS_DEBUG_DEFAULT = [
]

LINKFLAGS_RELEASE_DEFAULT = [
]

LINKFLAGS_DEBUG = LINKFLAGS_COMMON_DEFAULT + LINKFLAGS_DEBUG_DEFAULT
LINKFLAGS_RELEASE = LINKFLAGS_COMMON_DEFAULT + LINKFLAGS_RELEASE_DEFAULT

LINKFLAGS_PRX_DEFAULT = [
    '-nostartfiles',
]

LINKFLAGS_PRX = LINKFLAGS_PRX_DEFAULT

def getSourceDir(
):
    return SOURCE_DIR

def getHeaderDir(
):
    return HEADER_DIR

def getIncludes(
):
    return INCLUDES

def getTestincludes(
):
    return TEST_INCLUDES

def getTestlibpath(
):
    return TEST_LIBPATH

def getCxxflagsDebug(
):
    return CXXFLAGS_DEBUG

def getCxxflagsRelease(
):
    return CXXFLAGS_RELEASE

def getDefinesDebug(
):
    return DEFINES_DEBUG

def getDefinesRelease(
):
    return DEFINES_RELEASE

def getLinkflagsDebug(
):
    return LINKFLAGS_DEBUG

def getLinkflagsRelease(
):
    return LINKFLAGS_RELEASE

def getLinkflagsPrx(
):
    return LINKFLAGS_PRX

from .options import options
from .configure import configure

from .builder import *
