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

DEFINES_GCC_COMMON_DEFAULT = [
    'COMPILER_TYPE_GCC',
]

DEFINES_GCC_DEBUG_DEFAULT = [
    'DEBUG',
]

DEFINES_GCC_RELEASE_DEFAULT = [
]

DEFINES_GCC_DEBUG = DEFINES_GCC_COMMON_DEFAULT + DEFINES_GCC_DEBUG_DEFAULT
DEFINES_GCC_RELEASE = DEFINES_GCC_COMMON_DEFAULT + DEFINES_GCC_RELEASE_DEFAULT

DEFINES_MSVC_COMMON_DEFAULT = [
    'COMPILER_TYPE_MSVC',
]

DEFINES_MSVC_DEBUG_DEFAULT = [
    'DEBUG',
]

DEFINES_MSVC_RELEASE_DEFAULT = [
]

DEFINES_MSVC_DEBUG = DEFINES_MSVC_COMMON_DEFAULT + DEFINES_MSVC_DEBUG_DEFAULT
DEFINES_MSVC_RELEASE = DEFINES_MSVC_COMMON_DEFAULT + DEFINES_MSVC_RELEASE_DEFAULT

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

def getDefinesGccDebug(
):
    return DEFINES_GCC_DEBUG

def getDefinesGccRelease(
):
    return DEFINES_GCC_RELEASE

def getDefinesMsvcDebug(
):
    return DEFINES_MSVC_DEBUG

def getDefinesMsvcRelease(
):
    return DEFINES_MSVC_RELEASE

from .options import options
from .configure import configure

from .builder import *
