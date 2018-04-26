# -*- coding: utf-8 -*-

from taf import builder

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

    def test_generateSourceForDict(
        _self,
    ):
        _self.assertEqual(
            [
                'sourcedir/dir1/test1.txt',
                'sourcedir/dir1/test2.txt',
                'sourcedir/dir2/test1.txt',
                'sourcedir/dir2/test2.txt',
            ],
            builder.generateSource(
                {
                    'dir2' : [
                        'test2',
                        'test1',
                    ],
                    'dir1' : [
                        'test1',
                        'test2',
                    ],
                },
                'sourcedir',
                '.txt',
            ),
        )
