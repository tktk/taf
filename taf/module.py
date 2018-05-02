# -*- coding: utf-8 -*-

from . import taf

import importlib

DEPENDS = None
BUILDER = None
TARGET = None
SOURCE = None
LIB = None
USE = None

def initialize(
):
    global DEPENDS
    global BUILDER
    global TARGET
    global SOURCE
    global LIB
    global USE

    DEPENDS = None
    BUILDER = None
    TARGET = None
    SOURCE = None
    LIB = None
    USE = None

def importModule(
    _moduleName,
):
    initialize()

    importlib.import_module( taf.TSCRIPTS_DIR + '.' + _moduleName )
