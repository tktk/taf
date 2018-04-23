# -*- coding: utf-8 -*-

from . import configure
from . import taf

import unittest

class TestConfigure( unittest.TestCase ):
    def test_build(
        _self,
    ):
        context = _DummyContext()

        context.options.build = 'debug'

        configure( context )

        _self.assertEqual(
            'debug',
            context.env.taf[ 'BUILD' ],
        )

    def test_loadTools(
        _self,
    ):
        context = _DummyContext()

        taf.LOAD_TOOLS = [
            'testtools',
        ]

        context.options.build = 'debug'

        configure( context )

        _self.assertEqual(
            [ 'testtools' ],
            context.tools,
        )

    def test_buildModules(
        _self,
    ):
        context = _DummyContext()

        context.options.build = 'debug'
        context.options[ 'enable.testmodule' ] = True
        context.options[ 'enable.testmodule_disable' ] = False
        context.options.otheroption1 = True
        context.options.otheroption2 = False

        taf.TSCRIPTS_DIR = 'test.tscripts_configure'

        configure( context )

        _self.assertEqual(
            [ 'testmodule' ],
            context.env.taf[ 'BUILD_MODULES' ],
        )

    #TODO test_buildModules_dependModules

class _DummyOptions:
    def __setattr__(
        _self,
        _name,
        _value,
    ):
        _self.__dict__[ _name ] = _value

    def __getattr__(
        _self,
        _name,
    ):
        return _self.__dict__[ _name ]

    def __setitem__(
        _self,
        _name,
        _value,
    ):
        _self.__setattr__(
            _name,
            _value,
        )

class _DummyEnv:
    pass

class _DummyContext:
    def __init__(
        _self,
    ):
        _self.tools = []
        _self.options = _DummyOptions()
        _self.env = _DummyEnv()

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
