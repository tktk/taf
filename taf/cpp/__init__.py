# -*- coding: utf-8 -*-

INCLUDES = None

SOURCE_DIR = 'src'
HEADER_DIR = 'inc'

def getIncludes(
):
    return INCLUDES

def getHeaderDir(
):
    return HEADER_DIR

from .options import options
from .configure import configure

from .builder import *
