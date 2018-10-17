# -*- coding: utf-8 -*-

from taf import configure
from taf import taf

import unittest

class TestConfigure( unittest.TestCase ):
    def test_build(
        _self,
    ):
        context = _DummyContext()

        context.options.build = None
        context.options.withouttest = False

        configure( context )

        _self.assertEqual(
            'debug',
            context.env.taf[ 'BUILD' ],
        )

    def test_buildUserBuild(
        _self,
    ):
        context = _DummyContext()

        taf.BUILD = 'release'

        context.options.build = None
        context.options.withouttest = False

        configure( context )

        _self.assertEqual(
            'release',
            context.env.taf[ 'BUILD' ],
        )

    def test_buildFromOption(
        _self,
    ):
        context = _DummyContext()

        context.options.build = 'release'
        context.options.withouttest = False

        configure( context )

        _self.assertEqual(
            'release',
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
        context.options.withouttest = False

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
        context.options.withouttest = False
        context.options[ 'enable.module' ] = True
        context.options[ 'enable.module_disable' ] = False
        context.options.otheroption1 = True
        context.options.otheroption2 = False

        taf.TSCRIPTS_DIR = 'test.tscripts_configure'

        configure( context )

        _self.assertEqual(
            [ 'module' ],
            context.env.taf[ 'BUILD_MODULES' ],
        )

    def test_buildModules_dependModules(
        _self,
    ):
        context = _DummyContext()

        context.options.build = 'debug'
        context.options.withouttest = False
        context.options[ 'enable.module1' ] = True
        context.options[ 'enable.module_disable' ] = False
        context.options.otheroption1 = True
        context.options.otheroption2 = False

        taf.TSCRIPTS_DIR = 'test.tscripts_configure'

        configure( context )

        _self.assertEqual(
            [
                'module1',
                'module2',
                'module3',
            ],
            context.env.taf[ 'BUILD_MODULES' ],
        )

    def test_buildModules_withoutTestModules(
        _self,
    ):
        context = _DummyContext()

        context.options.withouttest = True
        context.options.build = 'debug'
        context.options[ 'enable.withtestmodule' ] = True

        taf.TSCRIPTS_DIR = 'test.tscripts_configure'

        configure( context )

        _self.assertEqual(
            [
                'withtestmodule',
                'module',
            ],
            context.env.taf[ 'BUILD_MODULES' ],
        )

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
