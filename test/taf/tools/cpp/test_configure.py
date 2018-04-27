# -*- coding: utf-8 -*-

from taf.tools.cpp import configure
from taf.tools import cpp

import unittest

class TestConfigure( unittest.TestCase ):
    def test_compilerTypeForLinux(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {}

        context.options.compilertype = None

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            'gcc',
            context.env.taf[ 'COMPILER_TYPE' ],
        )

    def test_linkerTypeForLinux(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {}

        context.options.linkertype = None

        context.options.compilertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            'ld',
            context.env.taf[ 'LINKER_TYPE' ],
        )

    def test_includes(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {}

        context.options.compilertype = None
        context.options.linkertype = None

        context.options.include = [
            'includedir1',
            'includedir2',
        ]

        configure( context )

        _self.assertEqual(
            [
                cpp.HEADER_DIR,
                'includedir1',
                'includedir2',
            ],
            context.env.INCLUDES,
        )

    def test_includesUserHeaderDir(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {}

        context.options.compilertype = None
        context.options.linkertype = None

        context.options.include = [
            'includedir1',
            'includedir2',
        ]

        cpp.HEADER_DIR = 'userinc'

        configure( context )

        _self.assertEqual(
            [
                'userinc',
                'includedir1',
                'includedir2',
            ],
            context.env.INCLUDES,
        )

    def test_cxxflagsGccDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {}

        context.options.compilertype = 'gcc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '-Wall',
                '-fno-rtti',
                '-fvisibility=hidden',
                '-std=c++14',
                '-O0',
                '-g',
            ],
            context.env.CXXFLAGS,
        )

    #TODO test_cxxflagsGccRelease
    #TODO test_cxxflagsMsvcDebug
    #TODO test_cxxflagsMsvcRelease
    #TODO test_definesGccDebug
    #TODO test_definesGccRelease
    #TODO test_definesMsvcDebug
    #TODO test_definesMsvcRelease
    #TODO test_linkflagsLdDebug
    #TODO test_linkflagsLdRelease
    #TODO test_linkflagsMsvcDebug
    #TODO test_linkflagsMsvcRelease

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
