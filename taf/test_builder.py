# -*- coding: utf-8 -*-

from . import builder

import unittest

class TestBuild( unittest.TestCase ):
    def test_generateSourceForString(
        _self,
    ):
        _self.assertEqual(
            [
                'sourcedir/test.txt'
            ],
            builder.generateSource(
                'test',
                'sourcedir',
                '.txt',
            ),
        )

    #TODO test_generateSourceForList
    #TODO test_generateSourceForDict
