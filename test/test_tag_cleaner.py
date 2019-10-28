# -*- coding: utf-8 -*-

import unittest
from source.tag_cleaner import TagCleaner
from os import getcwd

class TestTagCleaner(unittest.TestCase):
    def setUp(self):
        self.formtd = open('./test/fixtures/the_last.txt')
        self.mock_result = open('./test/fixtures/pure_text.txt')
        self.test = TagCleaner(self.formtd)
        self.maxDiff = None

    def test_clean(self):
        teste = self.assertEqual(self.test.clean(), self.mock_result.read())

    def tearDown(self):
        self.mock_result.close()
        self.formtd.close()

class TestBadPath(unittest.TestCase):
    def setUp(self):
        self.teste = TagCleaner('not_exist.txt')


if __name__ == '__main__':
    unittest.main()
