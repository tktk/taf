# -*- coding: utf-8 -*-

from . import taf

def loadTools(
    _context,
):
    LOAD_TOOLS = taf.LOAD_TOOLS

    if LOAD_TOOLS is not None:
        _context.load( LOAD_TOOLS )
