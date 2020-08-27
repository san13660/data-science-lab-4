
import pickle
import sys

print('Cargando archivo...')

file = open(sys.argv[1], encoding="utf8")
text = file.read()
text = text[0:10000000]

unique_words = set(text.split(' '))

print('Cargando modelo...')

with open(sys.argv[1].replace('.txt','_model.pickle'), 'rb') as input_file:
    model = pickle.load(input_file)

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