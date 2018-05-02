# -*- coding: utf-8 -*-

from ...options import optionKey

def options(
    _context,
):
    _addCompilerTypeOption( _context )
    _addLinkerTypeOption( _context )
    _addIncludesOption( _context )
    _addTestIncludesOption( _context )
    _addTestLibpathOption( _context )

def _addCompilerTypeOption(
    _context,
):
    _context.add_option(
        optionKey( 'compilertype' ),
        action = 'store',
        default = None,
    )

def _addLinkerTypeOption(
    _context,
):
    _context.add_option(
        optionKey( 'linkertype' ),
        action = 'store',
        default = None,
    )

def _addIncludesOption(
    _context,
):
    _context.add_option(
        optionKey( 'include' ),
        action = 'append',
        default = None,
    )

def _addTestIncludesOption(
    _context,
):
    _context.add_option(
        optionKey( 'testinclude' ),
        action = 'append',
        default = None,
    )

def _addTestLibpathOption(
    _context,
):
    _context.add_option(
        optionKey( 'testlibpath' ),
        action = 'append',
        default = None,
    )
