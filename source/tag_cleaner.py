# -*- coding: utf-8 -*-

from re import sub
from sys import argv

class TagCleaner:
    def __init__(self):
        self.path = argv[1] if argv[1:] else input("Path do Arquivo: ")

    def clean(self):
        with open('pure_text.txt', 'w') as pure:
            try:
                with open(self.path, 'r') as html:
                    for line in html:
                        pure.write(sub('<[^>]*>', '', line))
            except FileNotFoundError as error:
                print(error)
                return FileNotFoundError


if __name__ == '__main__':
    TagCleaner().clean()
