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
