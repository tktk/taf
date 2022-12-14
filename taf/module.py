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
USER_DATA = None

def initialize(
):
    global DEPENDS
    global TYPE
    global BUILDER
    global TARGET
    global SOURCE
    global LIB
    global USE
    global USER_DATA

    DEPENDS = None
    TYPE = None
    BUILDER = None
    TARGET = None
    SOURCE = None
    LIB = None
    USE = None
    USER_DATA = None

def importModule(
    _moduleName,
):
    initialize()

    importlib.reload( importlib.import_module( taf.TSCRIPTS_DIR + '.' + _moduleName ) )

def default(
):
    return taf.PACKAGE_NAME

def test(
):
    return taf.TEST_DIR

def tmp(
):
    return taf.TMP_DIR
