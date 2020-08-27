# Universidad del Valle de Guatemala
# Data Science 1 - Seccion 10
# Christopher Sandoval 13660
# Maria Fernanda Estrada 14198
# Estuardo Díaz 16110
# *
# 20/08/2020
# Programa para saber la cantidad de cada palabra en un archivo de texto y mostrar el top 10

# Liberias
import collections
import pandas as pd
import sys

# Leer un archivo indicado en la terminal
file = open(sys.argv[1], encoding="utf8")
text = file.read()

# Separar las palabras por espacio y contar una por una. Si todavia no esta en el diccionario, la agrega y suma 1. Si ya esta, solo suma 1
wordcount = {}
for word in text.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

# Mostrar las 10 palabras con mayor cantidad
n_print = 10
word_counter = collections.Counter(wordcount)
print('Palabras mas frecuentes: ')
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)

file.close()

# Colocar este listado en un csv para que sea mas facil leer y graficar un histograma
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.to_csv("frecuencia_palabras.csv")
