# -*- coding: utf-8 -*-

from .. import builder
from .. import taf

import os.path

def program(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    _context(
        features = [
            'cxx',
            'cxxprogram',
        ],
        target = _TARGET,
        source = builder.generateSource(
            _SOURCE,
            os.path.join(
                taf.SRC_DIR,
                taf.PACKAGE_NAME,
            ),
            '.cpp',
        ),
        lib = _LIB,
        use = _USE,
    )

def shlib(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    #TODO
    pass
#    _context(
#        features = [
#            'cxx',
#            'cxxshlib',
#        ],
#        target = _TARGET,
#        source = _SOURCE,
#        lib = _LIB,
#        use = _USE,
#    )

def gtest(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    #TODO
    pass
#    lib = []
#    lib.append( 'gtest' )
#    lib.extend( _LIB )
#
#    _context(
#        features = [
#            'cxx',
#            'cxxprogram',
#            'test',
#        ],
#        target = _TARGET,
#        source = _SOURCE,
#        lib = lib,
#        use = _USE,
#    )
