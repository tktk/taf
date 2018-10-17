# -*- coding: utf-8 -*-

from . import taf

import importlib

DEPENDS = None
TYPE = None
BUILDER = None
TARGET = None
SOURCE = None
LIB = None
USE = None

def initialize(
):
    global DEPENDS
    global TYPE
    global BUILDER
    global TARGET
    global SOURCE
    global LIB
    global USE

    DEPENDS = None
    TYPE = None
    BUILDER = None
    TARGET = None
    SOURCE = None
    LIB = None
    USE = None

def importModule(
    _moduleName,
):
    initialize()

    importlib.reload( importlib.import_module( taf.TSCRIPTS_DIR + '.' + _moduleName ) )

def test(
):
    return 'test'

def default(
):
    return taf.PACKAGE_NAME
