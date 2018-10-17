# -*- coding: utf-8 -*-

import os.path

def generateTarget(
    _DIR,
    _NAME,
):
    return os.path.join(
        _DIR,
        _NAME,
    )

def generateSource(
    _SOURCE,
    _PREFIX = None,
):
    source = []

    _generateSourceList(
        source,
        _SOURCE,
        _PREFIX,
    )

    source.sort()

    return source

def _generateSourceList(
    _sourceList,
    _SOURCE,
    _PREFIX,
):
    TYPE = type( _SOURCE )

    if TYPE is dict:
        _generateSourceListForDict(
            _sourceList,
            _SOURCE,
            _PREFIX,
        )
    elif TYPE is list:
        _generateSourceListForList(
            _sourceList,
            _SOURCE,
            _PREFIX,
        )
    else:
        _generateSourceListForString(
            _sourceList,
            _SOURCE,
            _PREFIX,
        )

def _generateSourceListForDict(
    _sourceList,
    _SOURCE_DICT,
    _PREFIX,
):
    for DIR, SOURCE in _SOURCE_DICT.items():
        prefix = None

        if _PREFIX is None:
            prefix = DIR
        else:
            prefix = os.path.join(
                _PREFIX,
                DIR,
            )

        _generateSourceList(
            _sourceList,
            SOURCE,
            prefix,
        )

def _generateSourceListForList(
    _sourceList,
    _SOURCE_LIST,
    _PREFIX,
):
    for SOURCE in _SOURCE_LIST:
        _generateSourceList(
            _sourceList,
            SOURCE,
            _PREFIX,
        )

def _generateSourceListForString(
    _sourceList,
    _SOURCE_STRING,
    _PREFIX,
):
    source = None

    if _PREFIX is None:
        source = _SOURCE_STRING
    else:
        source = os.path.join(
            _PREFIX,
            _SOURCE_STRING,
        )

    _sourceList.append( source )
