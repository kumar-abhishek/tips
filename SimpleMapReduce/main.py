#-*- coding=utf-8 -*-

#Ref: http://coreblog.org/ats/translation-of-implementing-mapreduce-with-python-multiprocessing-module/

import multiprocessing
import string

from multiprocessing_mapreduce import SimpleMapReduce

def file_to_words(filename):
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'for', 'if', 'in',
            'is', 'it', 'of', 'or', 'py', 'rst', 'the', 'to', 'with',
    ])
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    print(multiprocessing.current_process().name, 'reading', filename)
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'):
                continue
            line = line.translate(TR)
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append( (word, 1) )

    return output

def count_words(item):
    word, occurances = item
    return (word, sum(occurances))

if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('*.txt')

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    print(word_counts)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print('\nTOP 20 WORDS BY FREQUENCY\n')
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print('%-*s: %5s' % (longest+1, word, count))
