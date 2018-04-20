# -*- coding: utf-8 -*-

from . import build
from . import taf

import unittest
import sys

class TestBuild( unittest.TestCase ):
    def test_build(
        _self,
    ):
        context = _DummyContext()

        taf.TSCRIPTS_DIR = 'test.tscripts_build'

        taf.PACKAGE_NAME = 'test_build'

        context.env.taf = {}
        BUILD_MODULES = [
            'testmodule1',
            'testmodule2',
            'testmodule3',
        ]
        context.env.taf[ 'BUILD_MODULES' ] = BUILD_MODULES

        _unloadModules( BUILD_MODULES )

        build( context )

        _self.assertEqual(
            3,
            len( context.builds ),
        )

        builds0 = context.builds[ 0 ]
        _self.assertEqual(
            [
                'dummyfeature1',
                'dummyfeature2',
            ],
            builds0.features,
        )
        _self.assertEqual(
            'testmodule1',
            builds0.target,
        )
        _self.assertEqual(
            [
                'src/test_build/testmodule1/src1.cpp',
                'src/test_build/testmodule1/src2.cpp',
            ],
            builds0.source,
        )
        _self.assertEqual(
            [
                'module1lib1',
                'module1lib2',
            ],
            builds0.lib,
        )
        #TODO
        _self.assertEqual(
            [
                'module1use1',
                'module1use2',
            ],
            builds0.use,
        )

        builds1 = context.builds[ 1 ]
        _self.assertEqual(
            [
                'dummyfeature1',
                'dummyfeature2',
            ],
            builds1.features,
        )
        _self.assertEqual(
            'testmodule2',
            builds1.target,
        )
        _self.assertEqual(
            [
                'src/test_build/testmodule2/a/src1.cpp',
                'src/test_build/testmodule2/a/src2.cpp',
                'src/test_build/testmodule2/b/src1.cpp',
                'src/test_build/testmodule2/b/src2.cpp',
                'src/test_build/testmodule2/c/src1.cpp',
                'src/test_build/testmodule2/c/src2.cpp',
            ],
            builds1.source,
        )
        _self.assertEqual(
            [
                'module2lib1',
                'module2lib2',
            ],
            builds1.lib,
        )
        #TODO
        _self.assertEqual(
            [
                'module2use1',
                'module2use2',
            ],
            builds1.use,
        )

        builds2 = context.builds[ 2 ]
        _self.assertEqual(
            [
                'dummyfeature1',
                'dummyfeature2',
            ],
            builds2.features,
        )
        _self.assertEqual(
            'testmodule3',
            builds2.target,
        )
        _self.assertEqual(
            [
                'src/test_build/testmodule3/src1.cpp',
                'src/test_build/testmodule3/src2.cpp',
            ],
            builds2.source,
        )
        _self.assertEqual(
            [],
            builds2.lib,
        )
        #TODO
        _self.assertEqual(
            [],
            builds2.use,
        )

class _DummyOptions:
    pass

class _DummyEnv:
    pass

class _DummyBuild:
    def __init__(
        _self,
        _features,
        _target,
        _source,
        _lib,
        _use,
    ):
        _self.features = _features
        _self.target = _target
        _self.source = _source
        _self.lib = _lib
        _self.use = _use

class _DummyContext:
    def __init__(
        _self,
    ):
        _self.tools = []
        _self.options = _DummyOptions()
        _self.env = _DummyEnv()
        _self.builds = []

    def load(
        _self,
        _tools,
    ):
        _self.tools.extend( _tools )

    def msg(
        _self,
        _dummy1,
        _dummy2,
    ):
        pass

    def __call__(
        _self,
        features,
        target,
        source,
        lib,
        use,
    ):
        _self.builds.append(
            _DummyBuild(
                features,
                target,
                source,
                lib,
                use,
            )
        )

def _unloadModules(
    _MODULES,
):
    modules = sys.modules

    for module in _MODULES:
        modulePath = taf.TSCRIPTS_DIR + '.' + module

        if modulePath in modules:
            modules.pop( modulePath )
