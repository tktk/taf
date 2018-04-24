# -*- coding: utf-8 -*-

from .. import taf

def configure(
    _context,
):
    _context.env.INCLUDES = _generateIncludes( _context )

def _generateIncludes(
    _context,
):
    includes = []

    includes.append( taf.INC_DIR )

    INCLUDE_OPTION = _context.options.include
    if INCLUDE_OPTION is not None:
        includes.extend( INCLUDE_OPTION )

    _context.msg(
        'includes',
        includes,
    )

    return includes
