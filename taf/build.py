# -*- coding: utf-8 -*-

from . import taf
from . import module

import os.path

def build(
    _context,
):
    for moduleName in _context.env.taf[ 'BUILD_MODULES' ]:
        module.importModule( moduleName )

        MODULE_TYPE = module.TYPE
        moduleType = MODULE_TYPE if MODULE_TYPE is not None else module.default

        module.BUILDER(
            _context,
            moduleType(),
            module.TARGET,
            module.SOURCE,
            module.LIB,
            module.USE,
        )

    POST_FUNCTIONS = taf.POST_FUNCTIONS
    if POST_FUNCTIONS is not None:
        for FUNCTION in POST_FUNCTIONS:
            _context.add_post_fun( FUNCTION )
