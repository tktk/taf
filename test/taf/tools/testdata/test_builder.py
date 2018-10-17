# -*- coding: utf-8 -*-

from taf.tools import testdata
from taf import taf

import unittest
import os.path

class TestBuilder( unittest.TestCase ):
    def test_copy(
        _self,
    ):
        context = _DummyContext()

        taf.TEST_DIR = 'test'

        testdata.TESTDATA_DIR = 'testdata'

        testdata.copy(
            context,
            'test',
            'target',
            [
                'source2.txt',
                'source1.txt',
            ],
            None,
            None,
        )

        BUILD = context.builds[ 0 ]
        _self.assertIsNotNone( BUILD.rule )
        _self.assertEqual(
            os.path.join(
                'test',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                os.path.join(
                    'testdata',
                    'target',
                    'source1.txt',
                ),
                os.path.join(
                    'testdata',
                    'target',
                    'source2.txt',
                ),
            ],
            BUILD.source,
        )

    def test_copyUserTestDir(
        _self,
    ):
        context = _DummyContext()

        taf.TEST_DIR = 'usertest'

        testdata.TESTDATA_DIR = 'testdata'

        testdata.copy(
            context,
            'usertest',
            'target',
            [
                'source2.txt',
                'source1.txt',
            ],
            None,
            None,
        )

        BUILD = context.builds[ 0 ]
        _self.assertIsNotNone( BUILD.rule )
        _self.assertEqual(
            os.path.join(
                'usertest',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                os.path.join(
                    'testdata',
                    'target',
                    'source1.txt',
                ),
                os.path.join(
                    'testdata',
                    'target',
                    'source2.txt',
                ),
            ],
            BUILD.source,
        )

    def test_copyUserTestdataDir(
        _self,
    ):
        context = _DummyContext()

        taf.TEST_DIR = 'test'

        testdata.TESTDATA_DIR = 'usertestdata'

        testdata.copy(
            context,
            'test',
            'target',
            [
                'source2.txt',
                'source1.txt',
            ],
            None,
            None,
        )

        BUILD = context.builds[ 0 ]
        _self.assertIsNotNone( BUILD.rule )
        _self.assertEqual(
            os.path.join(
                'test',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                os.path.join(
                    'usertestdata',
                    'target',
                    'source1.txt',
                ),
                os.path.join(
                    'usertestdata',
                    'target',
                    'source2.txt',
                ),
            ],
            BUILD.source,
        )

class _DummyBuild:
    def __init__(
        _self,
        _rule,
        _target,
        _source,
    ):
        _self.rule = _rule
        _self.target = _target
        _self.source = _source

class _DummyContext:
    def __init__(
        _self,
    ):
        _self.builds = []

    def __call__(
        _self,
        rule,
        target,
        source,
    ):
        _self.builds.append(
            _DummyBuild(
                rule,
                target,
                source,
            )
        )
