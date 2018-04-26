# -*- coding: utf-8 -*-

from taf import options
from taf import taf

import unittest

class TestOptions( unittest.TestCase ):
    def test_build(
        _self,
    ):
        context = _DummyContext()

        taf.BUILD = 'debug'

        options( context )

        OPTION = _findOption(
            context,
            'build',
        )

        _self.assertEqual(
            _DummyOption(
                '--build',
                'store',
                'debug',
            ),
            OPTION,
        )

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

        OPTION = _findOption(
            context,
            'enable.module',
        )

        _self.assertEqual(
            _DummyOption(
                '--enable.module',
                'store_true',
                False,
            ),
            OPTION,
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

def _findOption(
    _context,
    _KEY,
):
    for OPTION in _context.options:
        if OPTION.key == '--' + _KEY:
            return OPTION

    return None

if __name__ == '__main__':
    unittest.main()
