# -*- coding: utf-8 -*-

from . import taf
from . import module

import importlib

def build(
    _context,
):
    for moduleName in _context.env.taf[ 'BUILD_MODULES' ]:
        module.initialize()

        importlib.import_module( taf.TSCRIPTS_DIR + '.' + moduleName )

        module.BUILDER(
            _context,
            module.TARGET,
            module.SOURCE,
            module.LIB,
            module.USE,
        )
