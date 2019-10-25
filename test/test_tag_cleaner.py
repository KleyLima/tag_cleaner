# -*- coding: utf-8 -*-

import unittest
from source.tag_cleaner import TagCleaner


class TestTagCleaner(unittest.TestCase):
    def test_clean(self):
        teste = TagCleaner().clean()
