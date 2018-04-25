# -*- coding: utf-8 -*-

import os.path

def generateSource(
    _SOURCE,
    _PREFIX,
    _SUFFIX,
):
    source = []

    _generateSourceList(
        source,
        _SOURCE,
        _PREFIX,
        _SUFFIX,
    )

    source.sort()

    return source

def _generateSourceList(
    _sourceList,
    _SOURCE,
    _PREFIX,
    _SUFFIX,
):
    TYPE = type( _SOURCE )

    if TYPE is dict:
        _generateSourceListForDict(
            _sourceList,
            _SOURCE,
            _PREFIX,
            _SUFFIX,
        )
    elif TYPE is list:
        _generateSourceListForList(
            _sourceList,
            _SOURCE,
            _PREFIX,
            _SUFFIX,
        )
    else:
        _generateSourceListForString(
            _sourceList,
            _SOURCE,
            _PREFIX,
            _SUFFIX,
        )

def _generateSourceListForDict(
    _sourceList,
    _SOURCE_DICT,
    _PREFIX,
    _SUFFIX,
):
    for DIR, SOURCE in _SOURCE_DICT.items():
        PREFIX = os.path.join(
            _PREFIX,
            DIR,
        )

        _generateSourceList(
            _sourceList,
            SOURCE,
            PREFIX,
            _SUFFIX,
        )

def _generateSourceListForList(
    _sourceList,
    _SOURCE_LIST,
    _PREFIX,
    _SUFFIX,
):
    for SOURCE in _SOURCE_LIST:
        _generateSourceList(
            _sourceList,
            SOURCE,
            _PREFIX,
            _SUFFIX,
        )

def _generateSourceListForString(
    _sourceList,
    _SOURCE_STRING,
    _PREFIX,
    _SUFFIX,
):
    _sourceList.append(
        os.path.join(
            _PREFIX,
            _SOURCE_STRING + _SUFFIX,
        )
    )
