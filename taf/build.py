# -*- coding: utf-8 -*-

from . import taf
from . import module

def build(
    _context,
):
    for moduleName in _context.env.taf[ 'BUILD_MODULES' ]:
        module.importModule( moduleName )

        module.BUILDER(
            _context,
            module.TARGET,
            module.SOURCE,
            module.LIB,
            module.USE,
        )

    POST_FUNCTIONS = taf.POST_FUNCTIONS
    if POST_FUNCTIONS is not None:
        for FUNCTION in POST_FUNCTIONS:
            _context.add_post_fun( FUNCTION )
