# -*- coding: utf-8 -*-

from . import configure
from . import taf

import unittest

class TestConfigure( unittest.TestCase ):
    def test_loadTools(
        _self,
    ):
        context = _DummyContext()

        taf.LOAD_TOOLS = [
            'testtools',
        ]

        configure( context )

        _self.assertEqual(
            [ 'testtools' ],
            context.tools,
        )

    def test_buildModules(
        _self,
    ):
        context = _DummyContext()

        context.options = {
            'enable.testmodule' : True,
            'enable.testmodule_disable' : False,
            'otheroption1' : True,
            'otheroption2' : False,
        }

        taf.TSCRIPTS_DIR = 'test.tscripts'

        configure( context )

        _self.assertEqual(
            [ 'testmodule' ],
            context.env.taf[ 'BUILD_MODULES' ],
        )

    #TODO test_buildModules_dependModules

class _DummyEnv:
    pass

class _DummyContext:
    def __init__(
        _self,
    ):
        _self.tools = []
        _self.options = {}
        _self.env = _DummyEnv()

    def load(
        _self,
        _tools,
    ):
        _self.tools.extend( _tools )
