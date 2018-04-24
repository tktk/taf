# -*- coding: utf-8 -*-

from . import common
from . import taf

from pydoc import ModuleScanner

def options(
    _context,
):
    _addBuildOptions( _context )
    _addModuleOptions( _context )

    common.loadTools( _context )

def _addBuildOptions(
    _context,
):
    _context.add_option(
        optionKey( 'build' ),
        action = 'store',
        default = taf.BUILD,
    )

def _addModuleOptions(
    _context,
):
    for module in _getModuleNames():
        _context.add_option(
            _optionModuleKey( module ),
            action = 'store_true',
            default = False,
        )

def _getModuleNames(
):
    TSCRIPTS_PREFIX = taf.TSCRIPTS_DIR + '.'

    modules = []
    ModuleScanner().run(
        lambda *args : modules.append( args[ 1 ] ),
        key = TSCRIPTS_PREFIX,
    )

    LENGTH = len( TSCRIPTS_PREFIX )

    return [ module[ LENGTH: ] for module in modules ]

def _optionModuleKey(
    _MODULE,
):
    return optionKey( common.MODULE_OPTION_PREFIX + _MODULE )

def optionKey(
    _NAME,
):
    return '--' + _NAME
