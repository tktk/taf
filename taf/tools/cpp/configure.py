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

def _getCompilerType(
    _context,
):
    compilerType = _context.options.compilertype

    if compilerType is None:
        compilerType = _getDefaultCompilerType()

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
