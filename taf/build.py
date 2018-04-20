# -*- coding: utf-8 -*-

from . import taf
from . import module

import importlib
import os.path

def build(
    _context,
):
    for moduleName in _context.env.taf[ 'BUILD_MODULES' ]:
        module.initialize()

        importlib.import_module( taf.TSCRIPTS_DIR + '.' + moduleName )

        SOURCE = _initializeSource()

        module.BUILDER(
            _context,
            module.TARGET,
            SOURCE,
            module.LIB,
            module.USE,
        )

def _initializeSource(
):
    source = []

    _generateSourceList(
        source,
        module.SOURCE,
        os.path.join(
            taf.SRC_DIR,
            taf.PACKAGE_NAME,
        ),
    )

    source.sort()

    return source

def _generateSourceList(
    _sourceList,
    _SOURCE,
    _PARENT,
):
    TYPE = type( _SOURCE )

    if TYPE is dict:
        _generateSourceListForDict(
            _sourceList,
            _SOURCE,
            _PARENT,
        )
    elif TYPE is list:
        _generateSourceListForList(
            _sourceList,
            _SOURCE,
            _PARENT,
        )
    else:
        _generateSourceListForString(
            _sourceList,
            _SOURCE,
            _PARENT,
        )

def _generateSourceListForDict(
    _sourceList,
    _SOURCE_DICT,
    _PARENT,
):
    for DIR, SOURCE in _SOURCE_DICT.items():
        PARENT = os.path.join(
            _PARENT,
            DIR,
        )

        _generateSourceList(
            _sourceList,
            SOURCE,
            PARENT,
        )

def _generateSourceListForList(
    _sourceList,
    _SOURCE_LIST,
    _PARENT,
):
    for SOURCE in _SOURCE_LIST:
        _generateSourceList(
            _sourceList,
            SOURCE,
            _PARENT,
        )

def _generateSourceListForString(
    _sourceList,
    _SOURCE_STRING,
    _PARENT,
):
    _sourceList.append(
        os.path.join(
            _PARENT,
            _SOURCE_STRING,
        )
    )
