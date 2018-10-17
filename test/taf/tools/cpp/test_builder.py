# -*- coding: utf-8 -*-

from taf.tools import cpp

import unittest

class TestBuilder( unittest.TestCase ):
    def test_program(
        _self,
    ):
        context = _DummyContext()

        cpp.SOURCE_DIR = 'src'

        cpp.program(
            context,
            'package',
            'target',
            [
                'source2.cpp',
                'source1.cpp',
            ],
            [
                'lib',
            ],
            [
                'use',
            ],
        )

        BUILD = context.builds[ 0 ]
        _self.assertEqual(
            [
                'cxx',
                'cxxprogram',
            ],
            BUILD.features,
        )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                'src/package/source1.cpp',
                'src/package/source2.cpp',
            ],
            BUILD.source,
        )
        _self.assertEqual(
            [ 'lib' ],
            BUILD.lib,
        )
        _self.assertEqual(
            [ 'use' ],
            BUILD.use,
        )

    def test_programNoneLib(
        _self,
    ):
        context = _DummyContext()

        cpp.SOURCE_DIR = 'src'

        cpp.program(
            context,
            'package',
            'target',
            [
                'source2.cpp',
                'source1.cpp',
            ],
            None,
            [
                'use',
            ],
        )

        BUILD = context.builds[ 0 ]
        _self.assertEqual(
            [
                'cxx',
                'cxxprogram',
            ],
            BUILD.features,
        )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                'src/package/source1.cpp',
                'src/package/source2.cpp',
            ],
            BUILD.source,
        )
        _self.assertEqual(
            [],
            BUILD.lib,
        )
        _self.assertEqual(
            [ 'use' ],
            BUILD.use,
        )

    def test_programNoneUse(
        _self,
    ):
        context = _DummyContext()

        cpp.SOURCE_DIR = 'src'

        cpp.program(
            context,
            'package',
            'target',
            [
                'source2.cpp',
                'source1.cpp',
            ],
            [
                'lib',
            ],
            None,
        )

        BUILD = context.builds[ 0 ]
        _self.assertEqual(
            [
                'cxx',
                'cxxprogram',
            ],
            BUILD.features,
        )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                'src/package/source1.cpp',
                'src/package/source2.cpp',
            ],
            BUILD.source,
        )
        _self.assertEqual(
            [ 'lib' ],
            BUILD.lib,
        )
        _self.assertEqual(
            [],
            BUILD.use,
        )

    def test_programUserSourceDir(
        _self,
    ):
        context = _DummyContext()

        cpp.SOURCE_DIR = 'usersrc'

        cpp.program(
            context,
            'package',
            'target',
            [
                'source2.cpp',
                'source1.cpp',
            ],
            [
                'lib',
            ],
            [
                'use',
            ],
        )

        BUILD = context.builds[ 0 ]
        _self.assertEqual(
            [
                'cxx',
                'cxxprogram',
            ],
            BUILD.features,
        )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                'usersrc/package/source1.cpp',
                'usersrc/package/source2.cpp',
            ],
            BUILD.source,
        )
        _self.assertEqual(
            [ 'lib' ],
            BUILD.lib,
        )
        _self.assertEqual(
            [ 'use' ],
            BUILD.use,
        )

    def test_shlib(
        _self,
    ):
        context = _DummyContext()

        cpp.SOURCE_DIR = 'src'

        cpp.shlib(
            context,
            'package',
            'target',
            [
                'source2.cpp',
                'source1.cpp',
            ],
            [
                'lib',
            ],
            [
                'use',
            ],
        )

        BUILD = context.builds[ 0 ]
        _self.assertEqual(
            [
                'cxx',
                'cxxshlib',
            ],
            BUILD.features,
        )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                'src/package/source1.cpp',
                'src/package/source2.cpp',
            ],
            BUILD.source,
        )
        _self.assertEqual(
            [ 'lib' ],
            BUILD.lib,
        )
        _self.assertEqual(
            [ 'use' ],
            BUILD.use,
        )

    def test_gtest(
        _self,
    ):
        context = _DummyContext()

        cpp.SOURCE_DIR = 'src'

        cpp.gtest(
            context,
            'package',
            'target',
            [
                'source2.cpp',
                'source1.cpp',
            ],
            [
                'lib',
            ],
            [
                'use',
            ],
        )

        BUILD = context.builds[ 0 ]
        _self.assertEqual(
            [
                'cxx',
                'cxxprogram',
                'test',
            ],
            BUILD.features,
        )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                'src/package/source1.cpp',
                'src/package/source2.cpp',
            ],
            BUILD.source,
        )
        _self.assertEqual(
            [
                'lib',
                'gtest',
            ],
            BUILD.lib,
        )
        _self.assertEqual(
            [
                'use',
                'TEST',
            ],
            BUILD.use,
        )

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
        _self.builds = []

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
