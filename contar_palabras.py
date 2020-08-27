import collections
import pandas as pd

import sys

file = open(sys.argv[1], encoding="utf8")
a= file.read()

wordcount = {}
for word in a.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1


n_print = 10
word_counter = collections.Counter(wordcount)
print('Palabras mas frecuentes: ')

for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)

file.close()

lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.to_csv("frecuencia_palabras.csv")