# -*- coding: utf-8 -*-

from taf.cpp import options
from taf import cpp

import unittest

class TestOptions( unittest.TestCase ):
    #TODO test_defines
    #TODO test_linkflags

    def test_includes(
        _self,
    ):
        context = _DummyContext()

        options( context )

        OPTION = _findOption(
            context,
            'include',
        )

        _self.assertEqual(
            _DummyOption(
                '--include',
                'append',
                None,
            ),
            OPTION,
        )

    def test_includes(
        _self,
    ):
        context = _DummyContext()

        cpp.INCLUDES = [
            'inc1',
            'inc2',
        ]

        options( context )

        OPTION = _findOption(
            context,
            'include',
        )

        _self.assertEqual(
            _DummyOption(
                '--include',
                'append',
                [
                    'inc1',
                    'inc2',
                ],
            ),
            OPTION,
        )

    #TODO test_libpath
    #TODO test_testlibpath

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
