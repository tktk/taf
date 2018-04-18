# -*- coding: utf-8 -*-

from . import common
from . import taf

def configure(
    _context,
):
    _context.env.taf = {}

    _context.env.taf[ 'BUILD_MODULES' ] = _generateBuildModules( _context )

    common.loadTools( _context )

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

    #TODO 依存モジュールの追加

#    module = _importModule( _MODULE )
#
#    DEPEND_MODULES = module.getDependModules()
#
#    for DEPEND_MODULE in DEPEND_MODULES:
#        _addBuildModules(
#            _buildModules,
#            DEPEND_MODULE,
#        )