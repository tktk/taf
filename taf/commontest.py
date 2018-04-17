# -*- coding: utf-8 -*-

from . import common
from . import taf

import unittest

class CommonTest( unittest.TestCase ):
    def testLoadTools(
        _self,
    ):
        context = CommonTestContext()

        taf.LOAD_TOOLS = [
            'testtools',
        ]

        common.loadTools( context )

        _self.assertEqual(
            [ 'testtools' ],
            context.tools,
        )

class CommonTestContext:
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
            Option(
                _key,
                action,
                default,
            )
        )

class Option:
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
