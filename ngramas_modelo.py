import nltk

from nltk.util import ngrams
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize, sent_tokenize
from nltk.lm import MLE
import pickle

import sys

print('Cargando archivo...')

file = open(sys.argv[1], encoding="utf8")
text = file.read()

text = text[0:10000000]

tokenized_text = [list(map(str.lower, word_tokenize(sent))) 
              for sent in sent_tokenize(text)]

print('Creando Modelo...')

n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)

model = MLE(n)
model.fit(train_data, padded_sents)

with open(sys.argv[1].replace('.txt','_model.pickle'), 'wb') as output_file:
    pickle.dump(model, output_file)

print('Modelo guardado (' + sys.argv[1].replace('.txt','_model.pickle') + ')')