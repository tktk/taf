# -*- coding: utf-8 -*-

from taf import module
from taf import taf

import unittest

class TestModule( unittest.TestCase ):
    def test_importModule(
        _self,
    ):
        taf.TSCRIPTS_DIR = 'test.tscripts_module'

        module.importModule( 'module1' )

        _self.assertEqual(
            [ 'depend1' ],
            module.DEPENDS
        )
        _self.assertEqual(
            'builder',
            module.BUILDER,
        )
        _self.assertEqual(
            'module1',
            module.TARGET,
        )
        _self.assertEqual(
            [
                'module1lib1',
                'module1lib2',
            ],
            module.LIB,
        )
        _self.assertEqual(
            [
                'module1use1',
                'module1use2',
            ],
            module.USE,
        )
