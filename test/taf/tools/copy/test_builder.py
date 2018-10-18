# -*- coding: utf-8 -*-

from taf.tools import copy

import unittest
import os.path

class TestBuilder( unittest.TestCase ):
    def test_files(
        _self,
    ):
        context = _DummyContext()

        copy.files(
            context,
            'package',
            'target',
            {
                'sourcedir' : [
                    'source2.txt',
                    'source1.txt',
                ],
            },
            None,
            None,
        )

        BUILD = context.builds[ 0 ]
        _self.assertIsNotNone( BUILD.rule )
        _self.assertEqual(
            os.path.join(
                'package',
                'target',
            ),
            BUILD.target,
        )
        _self.assertEqual(
            [
                os.path.join(
                    'sourcedir',
                    'source1.txt',
                ),
                os.path.join(
                    'sourcedir',
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
