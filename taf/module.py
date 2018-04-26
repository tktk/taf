# -*- coding: utf-8 -*-

DEPENDS = None
BUILDER = None
TARGET = None
SOURCE = None
LIB = []
USE = []

def initialize(
):
    global BUILDER
    global TARGET
    global SOURCE
    global LIB
    global USE

    BUILDER = None
    TARGET = None
    SOURCE = None
    LIB = []
    USE = []
