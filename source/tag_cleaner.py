# -*- coding: utf-8 -*-

from re import sub
from sys import argv

class TagCleaner:
    def __init__(self, path):
        self.path = path

    def clean(self):
        with open('pure_text.txt', 'w+') as pure:
            try:
                with open(self.path, 'r') as html:
                    for line in html:
                        pure.write(sub('<[^>]*>', '', line))
                    a = (pure.read())
                    print(type(a))
                    print(a)

            except FileNotFoundError as error:
                print(error)
                raise FileNotFoundError


if __name__ == '__main__':
    TagCleaner('/home/semantix/Workspace/Python/tag_cleaner/test/fixtures/the_last.txt').clean()

