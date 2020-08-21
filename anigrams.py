import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import re
import sys

text = ''
#with open(sys.argv[1], 'r', encoding='utf-8') as infile:
#    for line in infile:
#        text += line

text = 'I need to write a program in NLTK that breaks a corpus (a large collection of ' \
       'txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams.' \
       'I need to write a program in NLTK that breaks a corpus'

token = nltk.word_tokenize(text)
unigrams = ngrams(token, 1)
bigrams = ngrams(token, 2)
trigrams = ngrams(token, 3)

print(Counter(bigrams))