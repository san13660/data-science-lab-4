# Universidad del Valle de Guatemala
# Data Science 1 - Seccion 10
# Christopher Sandoval 13660
# Maria Fernanda Estrada 14198
# Estuardo Díaz 16110
# *
# 20/08/2020
# Programa para generar el modelo con n-gramas


# Librerias
import nltk
from nltk.util import ngrams
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize, sent_tokenize
from nltk.lm import MLE
import pickle
import sys

# Leer archivo ya preprocesado
print('Cargando archivo...')
file = open(sys.argv[1], encoding="utf8")
text = file.read()[0:10000000]

# Tokenizar para generar n-gramas
tokenized_text = [list(map(str.lower, word_tokenize(sent))) 
              for sent in sent_tokenize(text)]

# Crear n-gramas y modelo. Se calculan las probabilidaddes de cada n-grama
print('Creando Modelo...')

# Se entrena el modelo usando 3-gramas
n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)

model = MLE(n)
model.fit(train_data, padded_sents)

with open(sys.argv[1].replace('.txt','_model.pickle'), 'wb') as output_file:
    pickle.dump(model, output_file)

print('Modelo guardado (' + sys.argv[1].replace('.txt','_model.pickle') + ')')
