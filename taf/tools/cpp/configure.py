# -*- coding: utf-8 -*-

from . import *

from waflib import Utils

def configure(
    _context,
):
    _context.load( 'compiler_cxx' )

    _context.env.taf[ 'COMPILER_TYPE' ] = _getCompilerType( _context )
    _context.env.taf[ 'LINKER_TYPE' ] = _getLinkerType( _context )
    _context.env.INCLUDES = _generateIncludes( _context )
    _context.env.CXXFLAGS = _generateCxxflags( _context )
    _context.env.DEFINES = _generateDefines( _context )
    _context.env.LINKFLAGS = _generateLinkflags( _context )

def _getCompilerType(
    _context,
):
    compilerType = _context.options.compilertype

    if compilerType is None:
        compilerType = _getDefaultCompilerType()

    _context.msg(
        'compiler type',
        compilerType,
    )

    return compilerType

def _getDefaultCompilerType(
):
    compilerType = None

    PLATFORM = Utils.unversioned_sys_platform()
    if PLATFORM == 'linux':
        compilerType = 'gcc'
    elif PLATFORM == 'win32':
        compilerType = 'msvc'

    return compilerType

def _getLinkerType(
    _context,
):
    linkerType = _context.options.linkertype

    if linkerType is None:
        linkerType = _getDefaultLinkerType()

    _context.msg(
        'linker type',
        linkerType,
    )

    return linkerType

def _getDefaultLinkerType(
):
    linkerType = None

    PLATFORM = Utils.unversioned_sys_platform()
    if PLATFORM == 'linux':
        linkerType = 'ld'
    elif PLATFORM == 'win32':
        linkerType = 'msvc'

    return linkerType

def _generateIncludes(
    _context,
):
    includes = []

    includes.append( getHeaderDir() )

    INCLUDE_OPTION = _context.options.include
    if INCLUDE_OPTION is not None:
        includes.extend( INCLUDE_OPTION )

    _context.msg(
        'includes',
        includes,
    )

    return includes

def _generateCxxflags(
    _context,
):
    cxxflags = None

    COMPILER_TYPE = _context.env.taf[ 'COMPILER_TYPE' ]
    if COMPILER_TYPE == 'gcc':
        cxxflags = _generateCxxflagsGcc( _context )
    elif COMPILER_TYPE == 'msvc':
        cxxflags = _generateCxxflagsMsvc( _context )

    _context.msg(
        'cxxflags',
        cxxflags,
    )

    return cxxflags

def _generateCxxflagsGcc(
    _context,
):
    cxxflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        cxxflags = getCxxflagsGccDebug()
    elif BUILD == 'release':
        cxxflags = getCxxflagsGccRelease()

    return cxxflags

def _generateCxxflagsMsvc(
    _context,
):
    cxxflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        cxxflags = getCxxflagsMsvcDebug()
    elif BUILD == 'release':
        cxxflags = getCxxflagsMsvcRelease()

    return cxxflags

def _generateDefines(
    _context,
):
    defines = None

    COMPILER_TYPE = _context.env.taf[ 'COMPILER_TYPE' ]
    if COMPILER_TYPE == 'gcc':
        defines = _generateDefinesGcc( _context )
    elif COMPILER_TYPE == 'msvc':
        defines = _generateDefinesMsvc( _context )

    _context.msg(
        'defines',
        defines,
    )

    return defines

def _generateDefinesGcc(
    _context,
):
    defines = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        defines = getDefinesGccDebug()
    elif BUILD == 'release':
        defines = getDefinesGccRelease()

    return defines

def _generateDefinesMsvc(
    _context,
):
    defines = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        defines = getDefinesMsvcDebug()
    elif BUILD == 'release':
        defines = getDefinesMsvcRelease()

    return defines

def _generateLinkflags(
    _context,
):
    linkflags = None

    LINKER_TYPE = _context.env.taf[ 'LINKER_TYPE' ]
    if LINKER_TYPE == 'ld':
        linkflags = _generateLinkflagsLd( _context )
    elif LINKER_TYPE == 'msvc':
        linkflags = _generateLinkflagsMsvc( _context )

    _context.msg(
        'linkflags',
        linkflags,
    )

    return linkflags

def _generateLinkflagsLd(
    _context,
):
    linkflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        linkflags = getLinkflagsLdDebug()
    elif BUILD == 'release':
        linkflags = getLinkflagsLdRelease()

    return linkflags

def _generateLinkflagsMsvc(
    _context,
):
    linkflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        linkflags = getLinkflagsMsvcDebug()
    elif BUILD == 'release':
        linkflags = getLinkflagsMsvcRelease()

    return linkflags
