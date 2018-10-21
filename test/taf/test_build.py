# -*- coding: utf-8 -*-

from taf import build
from taf import taf

import unittest
import os.path

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
            'test_build',
            builds0.targetDir,
        )
        _self.assertEqual(
            'module1',
            builds0.targetName,
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
            'test_build',
            builds1.targetDir,
        )
        _self.assertEqual(
            'module2',
            builds1.targetName,
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
            'test_build',
            builds2.targetDir,
        )
        _self.assertEqual(
            'module3',
            builds2.targetName,
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
            None,
            builds2.use,
        )

    def test_buildTestModule(
        _self,
    ):
        context = _DummyContext()

        taf.TSCRIPTS_DIR = 'test.tscripts_build'

        taf.PACKAGE_NAME = 'test_build'

        context.env.taf = {}
        context.env.taf[ 'BUILD_MODULES' ] = [
            'testmodule',
        ]

        build( context )

        _self.assertEqual(
            1,
            len( context.builds ),
        )

        builds0 = context.builds[ 0 ]
        _self.assertEqual(
            [
                'dummyfeature',
            ],
            builds0.features,
        )
        _self.assertEqual(
            'test',
            builds0.targetDir,
        )
        _self.assertEqual(
            'testmodule',
            builds0.targetName,
        )
        _self.assertEqual(
            {
                'testmodule' : [
                    'src.cpp',
                ],
            },
            builds0.source,
        )
        _self.assertEqual(
            None,
            builds0.lib,
        )
        _self.assertEqual(
            None,
            builds0.use,
        )

    def test_buildWithUserData(
        _self,
    ):
        context = _DummyContext()

        taf.TSCRIPTS_DIR = 'test.tscripts_build'

        taf.PACKAGE_NAME = 'test_buildwithuserdata'

        context.env.taf = {}
        context.env.taf[ 'BUILD_MODULES' ] = [
            'modulewithuserdata',
        ]

        build( context )

        _self.assertEqual(
            1,
            len( context.builds ),
        )

        builds0 = context.builds[ 0 ]
        _self.assertEqual(
            'dummyfeature',
            builds0.features,
        )
        _self.assertEqual(
            'test_buildwithuserdata',
            builds0.targetDir,
        )
        _self.assertEqual(
            'modulewithuserdata',
            builds0.targetName,
        )
        _self.assertEqual(
            'src.cpp',
            builds0.source,
        )
        _self.assertEqual(
            'lib',
            builds0.lib,
        )
        _self.assertEqual(
            'use',
            builds0.use,
        )
        _self.assertEqual(
            {
                'USER_DATA' : [
                    'data1',
                    'data2',
                ]
            },
            builds0.userData,
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
        _targetDir,
        _targetName,
        _source,
        _lib,
        _use,
        _userData,
    ):
        _self.features = _features
        _self.targetDir = _targetDir
        _self.targetName = _targetName
        _self.source = _source
        _self.lib = _lib
        _self.use = _use
        _self.userData = _userData

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
        targetDir,
        targetName,
        source,
        lib,
        use,
        userData = None,
    ):
        _self.builds.append(
            _DummyBuild(
                features,
                targetDir,
                targetName,
                source,
                lib,
                use,
                userData,
            )
        )
