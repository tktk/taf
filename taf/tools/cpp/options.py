# -*- coding: utf-8 -*-

from . import *
from ...options import optionKey

def options(
    _context,
):
    _addIncludesOption( _context )

def _addIncludesOption(
    _context,
):
    _context.add_option(
        optionKey( 'include' ),
        action = 'append',
        default = getIncludes(),
    )
