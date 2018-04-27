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

CXXFLAGS_MSVC_COMMON_DEFAULT = [
    '/Wall',
    '/GR-',
    '/nologo',
    '/EHs',
]

CXXFLAGS_MSVC_DEBUG_DEFAULT = [
    '/MDd',
    '/Od',
]

CXXFLAGS_MSVC_RELEASE_DEFAULT = [
    '/MD',
    '/O2',
    '/Oi',
    '/GL',
]

CXXFLAGS_MSVC_DEBUG = CXXFLAGS_MSVC_COMMON_DEFAULT + CXXFLAGS_MSVC_DEBUG_DEFAULT
CXXFLAGS_MSVC_RELEASE = CXXFLAGS_MSVC_COMMON_DEFAULT + CXXFLAGS_MSVC_RELEASE_DEFAULT

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

def getCxxflagsMsvcDebug(
):
    return CXXFLAGS_MSVC_DEBUG

def getCxxflagsMsvcRelease(
):
    return CXXFLAGS_MSVC_RELEASE

from .options import options
from .configure import configure

from .builder import *
