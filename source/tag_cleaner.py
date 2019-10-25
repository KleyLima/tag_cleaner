# -*- coding: utf-8 -*-

from re import sub
from sys import argv

class TagCleaner:
    def clean(self):
        with open('pure_text.txt', 'w') as pure:
            with open(argv[1], 'r') as html:
                for line in html:
                    pure.write(sub('<[^>]*>', '', line))

                    


if __name__ == '__main__':
    TagCleaner().clean()
