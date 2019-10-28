# -*- coding: utf-8 -*-

from sys import argv, stdin

class TagCleaner:
    def __init__(self, text):
        self.text = text

        for line in self.text:
            print(line.strip())

if __name__ == '__main__':
    print(stdin)
    TagCleaner(stdin)

