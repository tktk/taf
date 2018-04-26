# -*- coding: utf-8 -*-

from . import common
from . import module

def build(
    _context,
):
    for moduleName in _context.env.taf[ 'BUILD_MODULES' ]:
        common.importModule( moduleName )

        module.BUILDER(
            _context,
            module.TARGET,
            module.SOURCE,
            module.LIB,
            module.USE,
        )
