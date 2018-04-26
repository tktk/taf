# -*- coding: utf-8 -*-

from taf import common
from taf import taf

import unittest

class TestCommon( unittest.TestCase ):
    def test_loadTools(
        _self,
    ):
        context = _DummyContext()

        taf.LOAD_TOOLS = [
            'testtools',
        ]

        common.loadTools( context )

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
