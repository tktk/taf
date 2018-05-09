# -*- coding: utf-8 -*-

from . import taf
from . import module

import importlib

MODULE_OPTION_PREFIX = 'enable.'

def loadTools(
    _context,
):
    LOAD_TOOLS = taf.LOAD_TOOLS

    if LOAD_TOOLS is not None:
        _context.load( LOAD_TOOLS )
