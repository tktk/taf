# -*- coding: utf-8 -*-

from . import options
from . import taf

import unittest

class TestOptions( unittest.TestCase ):
    def test_loadTools(
        _self,
    ):
        context = _DummyContext()

        taf.LOAD_TOOLS = [
            'testtools',
        ]

        options( context )

        _self.assertEqual(
            [ 'testtools' ],
            context.tools,
        )

    def test_moduleOptions(
        _self,
    ):
        context = _DummyContext()

        taf.TSCRIPTS_DIR = 'test.tscripts_options'

        options( context )

        _self.assertEqual(
            [
                _DummyOption(
                    '--enable.testmodule',
                    'store_true',
                    False,
                ),
            ],
            context.options,
        )

class _DummyContext:
    def __init__(
        _self,
    ):
        _self.tools = []
        _self.options = []

    def load(
        _self,
        _tools,
    ):
        _self.tools.extend( _tools )

    def add_option(
        _self,
        _key,
        action,
        default,
    ):
        _self.options.append(
            _DummyOption(
                _key,
                action,
                default,
            )
        )

class _DummyOption:
    def __init__(
        _self,
        _key,
        _action,
        _default,
    ):
        _self.key = _key
        _self.action = _action
        _self.default = _default

    def __eq__(
        _SELF,
        _OTHER,
    ):
        if _SELF.key != _OTHER.key:
            return False

        if _SELF.action != _OTHER.action:
            return False

        if _SELF.default != _OTHER.default:
            return False

        return True

if __name__ == '__main__':
    unittest.main()
