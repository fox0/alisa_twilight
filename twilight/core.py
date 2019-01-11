#!/usr/bin/env python3
import re
import logging
import pymorphy2

log = logging.getLogger(__name__)

morph = pymorphy2.MorphAnalyzer()


def prosess(tokens):
    for word in tokens:
        for i in morph.parse(word):
            print(i.tag.cyr_repr, i)
            if i.score > 0.33:
                break
        print()

    print(morph.parse('стол')[0].inflect({morph.cyr2lat('рд')}))
    return ' '.join(tokens)


def str2tokens(text):
    return re.findall(r'\w+', text)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(funcName)s:%(name)s:%(lineno)d: %(message)s',
                        level=logging.DEBUG)
    # import django
    # django.setup()
    while True:
        line = input('> ')
        tokens = str2tokens(line)
        print(prosess(tokens))
