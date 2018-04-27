# -*- coding: utf-8 -*-

from . import *
from ...options import optionKey

def options(
    _context,
):
    _context.load( 'compiler_cxx' )

    _addCompilerTypeOption( _context )
    _addIncludesOption( _context )

def _addCompilerTypeOption(
    _context,
):
    _context.add_option(
        optionKey( 'compilertype' ),
        action = 'store',
        default = None,
    )

def _addIncludesOption(
    _context,
):
    _context.add_option(
        optionKey( 'include' ),
        action = 'append',
        default = getIncludes(),
    )
