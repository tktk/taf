# -*- coding: utf-8 -*-

from taf.tools import builder

import unittest

class TestBuild( unittest.TestCase ):
    def test_generateSourceForString(
        _self,
    ):
        _self.assertEqual(
            [
                'sourcedir/test.txt',
            ],
            builder.generateSource(
                'test.txt',
                'sourcedir',
            ),
        )

    def test_generateSourceForStringWithoutPrefix(
        _self,
    ):
        _self.assertEqual(
            [
                'test.txt',
            ],
            builder.generateSource(
                'test.txt',
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
                    'test1.txt',
                    'test3.txt',
                    'test2.txt',
                ],
                'sourcedir',
            ),
        )

    def test_generateSourceForListWithoutPrefix(
        _self,
    ):
        _self.assertEqual(
            [
                'test1.txt',
                'test2.txt',
                'test3.txt',
            ],
            builder.generateSource(
                [
                    'test1.txt',
                    'test3.txt',
                    'test2.txt',
                ],
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
                        'test2.txt',
                        'test1.txt',
                    ],
                    'dir1' : [
                        'test1.txt',
                        'test2.txt',
                    ],
                },
                'sourcedir',
            ),
        )

    def test_generateSourceForDictWithoutPrefix(
        _self,
    ):
        _self.assertEqual(
            [
                'dir1/test1.txt',
                'dir1/test2.txt',
                'dir2/test1.txt',
                'dir2/test2.txt',
            ],
            builder.generateSource(
                {
                    'dir2' : [
                        'test2.txt',
                        'test1.txt',
                    ],
                    'dir1' : [
                        'test1.txt',
                        'test2.txt',
                    ],
                },
            ),
        )
