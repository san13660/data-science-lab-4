import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import re
import sys

#Funcion para calcular unigramas y frecuencias
def calcular_frecuencias_unigrama(sequence):
    print (sequence)
    uniques=[]
    for i in sequence:
        if (i not in uniques):
            uniques.append(i)
    cants = []
    for i in uniques:
        cants.append(sequence.count(i))
    final =[]
    for i in range(len(uniques)-1):
        a=[]
        a.append(uniques[i])
        a.append(cants[i])
        final.append(a)
    return final

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
