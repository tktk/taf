# -*- coding: utf-8 -*-

INCLUDES = None

SOURCE_DIR = 'src'
HEADER_DIR = 'inc'

def getIncludes(
):
    return INCLUDES

from .options import options
from .configure import configure

from .builder import *
