# Universidad del Valle de Guatemala
# Data Science 1 - Seccion 10
# Christopher Sandoval 13660
# Maria Fernanda Estrada 14198
# Estuardo Díaz 16110
# *
# 20/08/2020
# Programa para graficar el top 10 de palabras mas frecuentes

# Librerias
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Leer y mostrar las palabras mas frecuentes en un histograma
df = pd.read_csv(sys.argv[1])
df.plot.bar(x='Word',y='Count')
plt.show()
