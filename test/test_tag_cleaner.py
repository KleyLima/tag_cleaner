# -*- coding: utf-8 -*-

import unittest
from source.tag_cleaner import TagCleaner
from os import getcwd

class TestTagCleaner(unittest.TestCase):
    def setUp(self):
        print(getcwd())
        self.teste = TagCleaner('./test/fixtures/the_last.txt')

    def test_clean(self):
        teste = self.teste.clean()

class TestBadPath(unittest.TestCase):
    def setUp(self):
        self.teste = TagCleaner('not_exist.txt')

    def test_bad_file(self):
        with self.assertRaises(FileNotFoundError):
            self.teste.clean()

if __name__ == '__main__':
    unittest.main()
