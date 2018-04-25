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

    def test_generateSourceForList(
        _self,
    ):
        _self.assertEqual(
            [
                'sourcedir/test1.txt',
                'sourcedir/test2.txt',
                'sourcedir/test3.txt',
            ],
            builder.generateSource(
                [
                    'test1',
                    'test3',
                    'test2',
                ],
                'sourcedir',
                '.txt',
            ),
        )

    #TODO test_generateSourceForDict
