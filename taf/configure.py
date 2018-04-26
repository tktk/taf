# -*- coding: utf-8 -*-

from . import common
from . import module

def configure(
    _context,
):
    _context.env.taf = {}

    _context.env.taf[ 'BUILD' ] = _getBuild( _context )
    _context.env.taf[ 'BUILD_MODULES' ] = _generateBuildModules( _context )

    common.loadTools( _context )

def _getBuild(
    _context,
):
    BUILD = _context.options.build

    _context.msg(
        'build',
        BUILD,
    )

    return BUILD

def _generateBuildModules(
    _context,
):
    buildModules = []

    MODULE_OPTION_PREFIX_LENGTH = len( common.MODULE_OPTION_PREFIX )

    for key, value in vars( _context.options ).items():
        if key[ :MODULE_OPTION_PREFIX_LENGTH ] != common.MODULE_OPTION_PREFIX:
            continue
        if value == False:
            continue

        MODULE = key[ MODULE_OPTION_PREFIX_LENGTH: ]

        _addBuildModules(
            buildModules,
            MODULE,
        )

    _context.msg(
        'build modules',
        buildModules,
    )

    return buildModules

def _addBuildModules(
    _buildModules,
    _MODULE,
):
    if _MODULE in _buildModules:
        return

    _buildModules.append( _MODULE )

    common.importModule( _MODULE )

    DEPENDS = module.DEPENDS

    if DEPENDS is not None:
        for DEPEND_MODULE in DEPENDS:
            _addBuildModules(
                _buildModules,
                DEPEND_MODULE,
            )
