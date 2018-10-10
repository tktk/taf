# -*- coding: utf-8 -*-

from ...options import optionKey

def options(
    _context,
):
    _addPspdevOption( _context )
    _addIncludesOption( _context )

def _addPspdevOption(
    _context,
):
    _context.add_option(
        optionKey( 'pspdev' ),
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
