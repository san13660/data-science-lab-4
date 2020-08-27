# Universidad del Valle de Guatemala
# Data Science 1 - Seccion 10
# Christopher Sandoval 13660
# Maria Fernanda Estrada 14198
# Estuardo Díaz 16110
# *
# 20/08/2020
# Programa para predecir (probar el modelo generado)


# Librerias
import pickle
import sys

# Leer el archivo que contiene el modelo y cargarlo
print('Cargando archivo...')
file = open(sys.argv[1], encoding="utf8")
text = file.read()[0:10000000]
unique_words = set(text.split(' '))

# Cargar modelo usando la libreria pickle
print('Cargando modelo...')
with open(sys.argv[1].replace('.txt','_model.pickle'), 'rb') as input_file:
    model = pickle.load(input_file)

# Leer las palabras que ingresa el usuario. Mostrar el top 5 de predicciones con su palabra y su probabilidad.
while(1):
    context = input('\nInserte las palabras: ')

    predictions = []

    for word in unique_words:
        new_prediction = {
                'palabra': word,
                'probabilidad': model.score(word, context.split())
            }
        if len(predictions) == 0:
            predictions.append(new_prediction)
        else:
            for index in range(len(predictions)):
                if(new_prediction['probabilidad'] >= predictions[index]['probabilidad']):
                    predictions.insert(index, new_prediction)
                    break
            
            if(len(predictions)>5):
                predictions = predictions[0:5]

    for prediction in predictions:
        print(prediction)
