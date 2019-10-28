# -*- coding: utf-8 -*-

from re import sub
from sys import argv, stdin


class TagCleaner:
    def __init__(self, text):
        self.text = text

    def clean(self):
        with open('pure_text.txt', 'w+') as pure:
            edited = ''
            for line in self.text:
                edited += (sub('<[^>]*>', '', line)
                pure.write(sub('<[^>]*>', '', line)
        return edited


if __name__ == '__main__':
    TagCleaner(stdin).clean()

