# -*- coding: utf-8 -*-

from . import common
from . import taf
from . import module

def configure(
    _context,
):
    _context.env.taf = {}

    _context.env.taf[ 'BUILD' ] = _getBuild( _context )

    WITHOUT_TEST = _getWithouttest( _context )

    _context.env.taf[ 'BUILD_MODULES' ] = _generateBuildModules(
        _context,
        WITHOUT_TEST,
    )

    common.loadTools( _context )

def _getBuild(
    _context,
):
    build = _context.options.build

    if build is None:
        build = taf.BUILD

    _context.msg(
        'build',
        build,
    )

    return build

def _getWithouttest(
    _context,
):
    withouttest = _context.options.withouttest

    if withouttest is None:
        withouttest = False

    _context.msg(
        'withouttest',
        withouttest,
    )

    return withouttest

def _generateBuildModules(
    _context,
    _WITHOUT_TEST,
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
            _WITHOUT_TEST,
        )

    _context.msg(
        'build modules',
        buildModules,
    )

    return buildModules

def _addBuildModules(
    _buildModules,
    _MODULE,
    _WITHOUT_TEST,
):
    if _MODULE in _buildModules:
        return

    module.importModule( _MODULE )

    if _WITHOUT_TEST == True and module.TYPE == module.test:
        return

    _buildModules.append( _MODULE )

    DEPENDS = module.DEPENDS

    if DEPENDS is not None:
        for DEPEND_MODULE in DEPENDS:
            _addBuildModules(
                _buildModules,
                DEPEND_MODULE,
                _WITHOUT_TEST,
            )
