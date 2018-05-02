# -*- coding: utf-8 -*-

from taf import build
from taf import taf

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
        context.env.taf[ 'BUILD_MODULES' ] = [
            'module1',
            'module2',
            'module3',
        ]

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
            'module1',
            builds0.target,
        )
        _self.assertEqual(
            {
                'module1' : [
                    'src1.cpp',
                    'src2.cpp',
                ],
            },
            builds0.source,
        )
        _self.assertEqual(
            [
                'module1lib1',
                'module1lib2',
            ],
            builds0.lib,
        )
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
            'module2',
            builds1.target,
        )
        _self.assertEqual(
            {
                'module2' : {
                    'c' : [
                        'src2.cpp',
                        'src1.cpp',
                    ],
                    'b' : [
                        'src2.cpp',
                        'src1.cpp',
                    ],
                    'a' : [
                        'src2.cpp',
                        'src1.cpp',
                    ],
                },
            },
            builds1.source,
        )
        _self.assertEqual(
            [
                'module2lib1',
                'module2lib2',
            ],
            builds1.lib,
        )
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
            'module3',
            builds2.target,
        )
        _self.assertEqual(
            {
                'module3' : [
                    'src1.cpp',
                    'src2.cpp',
                ],
            },
            builds2.source,
        )
        _self.assertEqual(
            None,
            builds2.lib,
        )
        _self.assertEqual(
            [],
            builds2.use,
        )

    def test_addPostFunctions(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {}
        context.env.taf[ 'BUILD_MODULES' ] = []

        build( context )

        _self.assertEqual(
            [],
            context.postFunctions,
        )

    def test_addPostFunctionsUserPostFunctions(
        _self,
    ):
        context = _DummyContext()

        taf.POST_FUNCTIONS = [
            'postfunction1',
            'postfunction2',
        ]

        context.env.taf = {}
        context.env.taf[ 'BUILD_MODULES' ] = []

        build( context )

        _self.assertEqual(
            [
                'postfunction1',
                'postfunction2',
            ],
            context.postFunctions,
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
        _self.postFunctions = []

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

    def add_post_fun(
        _self,
        _FUNCTION,
    ):
        _self.postFunctions.append( _FUNCTION )

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
