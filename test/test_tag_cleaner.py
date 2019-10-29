# -*- coding: utf-8 -*-

import unittest
from source.tag_cleaner import TagCleaner
from os import getcwd

class TestCleanLast(unittest.TestCase):
    def setUp(self):
        self.formtd = open('./test/fixtures/the_last.txt')
        self.mock_result = open('./test/fixtures/pure_last.txt')
        self.test = TagCleaner(self.formtd)
        print('Testing the_last.txt')

    def test_clean(self):
        self.assertEqual(self.test.clean(), self.mock_result.read())

    def tearDown(self):
        self.mock_result.close()
        self.formtd.close()

class TestCleanStack(unittest.TestCase):
    def setUp(self):
        self.formtd = open('./test/fixtures/stack.txt')
        self.mock_result = open('./test/fixtures/pure_stack.txt')
        self.test = TagCleaner(self.formtd)
        print('Testing stack.txt')

    def test_clean(self):
        self.assertEqual(self.test.clean(), self.mock_result.read())

    def tearDown(self):
        self.mock_result.close()
        self.formtd.close()


if __name__ == '__main__':
    unittest.main()
