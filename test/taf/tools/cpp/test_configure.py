# -*- coding: utf-8 -*-

from taf.tools.cpp import configure
from taf.tools import cpp

import unittest

class TestConfigure( unittest.TestCase ):
    def test_compilerTypeForLinux(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

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

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.linkertype = None

        context.options.compilertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            'ld',
            context.env.taf[ 'LINKER_TYPE' ],
        )

    #TODO 初期値の場合のテストを追加する
    def test_includes(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.include = [
            'includedir1',
            'includedir2',
        ]

        context.options.compilertype = None
        context.options.linkertype = None

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

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.include = [
            'includedir1',
            'includedir2',
        ]

        cpp.HEADER_DIR = 'userinc'

        context.options.compilertype = None
        context.options.linkertype = None

        configure( context )

        _self.assertEqual(
            [
                'userinc',
                'includedir1',
                'includedir2',
            ],
            context.env.INCLUDES,
        )

    def test_testlibpath(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.testlibpath = None

        context.options.compilertype = None
        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertIs(
            None,
            context.env.LIBPATH_TEST,
        )

        _self.assertIs(
            None,
            context.env.RPATH_TEST,
        )

    def test_cxxflagsGccDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

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

    def test_cxxflagsGccRelease(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'release',
        }

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
                '-O2',
            ],
            context.env.CXXFLAGS,
        )

    def test_cxxflagsMsvcDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.compilertype = 'msvc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '/Wall',
                '/GR-',
                '/nologo',
                '/EHs',
                '/MDd',
                '/Od',
            ],
            context.env.CXXFLAGS,
        )

    def test_cxxflagsMsvcRelease(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'release',
        }

        context.options.compilertype = 'msvc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '/Wall',
                '/GR-',
                '/nologo',
                '/EHs',
                '/MD',
                '/O2',
                '/Oi',
                '/GL',
            ],
            context.env.CXXFLAGS,
        )

    def test_definesGccDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.compilertype = 'gcc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                'COMPILER_TYPE_GCC',
                'DEBUG',
            ],
            context.env.DEFINES,
        )

    def test_definesGccRelease(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'release',
        }

        context.options.compilertype = 'gcc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                'COMPILER_TYPE_GCC',
            ],
            context.env.DEFINES,
        )

    def test_definesMsvcDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.compilertype = 'msvc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                'COMPILER_TYPE_MSVC',
                'DEBUG',
            ],
            context.env.DEFINES,
        )

    def test_definesMsvcRelease(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'release',
        }

        context.options.compilertype = 'msvc'

        context.options.linkertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                'COMPILER_TYPE_MSVC',
            ],
            context.env.DEFINES,
        )

    def test_linkflagsLdDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.linkertype = 'ld'

        context.options.compilertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '-pthread',
            ],
            context.env.LINKFLAGS,
        )

    def test_linkflagsLdRelease(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'release',
        }

        context.options.linkertype = 'ld'

        context.options.compilertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '-pthread',
            ],
            context.env.LINKFLAGS,
        )

    def test_linkflagsMsvcDebug(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'debug',
        }

        context.options.linkertype = 'msvc'

        context.options.compilertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '/NOLOGO',
                '/DYNAMICBASE',
                '/NXCOMPAT',
            ],
            context.env.LINKFLAGS,
        )

    def test_linkflagsMsvcRelease(
        _self,
    ):
        context = _DummyContext()

        context.env.taf = {
            'BUILD' : 'release',
        }

        context.options.linkertype = 'msvc'

        context.options.compilertype = None
        context.options.include = None

        configure( context )

        _self.assertEqual(
            [
                '/NOLOGO',
                '/DYNAMICBASE',
                '/NXCOMPAT',
                '/OPT:REF',
                '/OPT:ICF',
                '/LTCG',
            ],
            context.env.LINKFLAGS,
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
