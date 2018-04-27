# -*- coding: utf-8 -*-

from . import *

def configure(
    _context,
):
    _context.load( 'compiler_cxx' )

    _context.env.INCLUDES = _generateIncludes( _context )

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
