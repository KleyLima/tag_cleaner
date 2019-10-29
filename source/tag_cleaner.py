# -*- coding: utf-8 -*-

from re import sub
from sys import argv, stdin


class TagCleaner:
    def __init__(self, text):
        self.text = text

    def clean(self):
        edited = ''
        for line in self.text:
            edited += sub('<[^>]*>', '', line)
        edited += '\n'
        return edited


if __name__ == '__main__':
    #print(TagCleaner(open('../test/fixtures/the_last.txt')).clean())
    print(TagCleaner(open('../test/fixtures/stack.txt')).clean())

