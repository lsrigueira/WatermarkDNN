# first neural network with keras tutorial
from datetime import time, datetime
from logging import PlaceHolder
from statistics import mode
import sys
import keras
import funcitions
from numpy import loadtxt, size
from keras.models import Sequential
from keras.layers import Dense
from typing import Sequence
import funcitions
import argparse   

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--rc', required=False, help='Recompile to changes DNN Weights', action='store_true')
parser.add_argument('--save', required=False, help='Set the new model as the default one', action='store_true')
parser.add_argument('-load',metavar='filepath', type=str, required=False, dest="filepath", help='Set the new model as the default one')

args = parser.parse_args()
print(funcitions.toBinary("secre_key"))

# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
print("All nice")
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model

if(args.rc):
    model = Sequential()
    model.add(Dense(500, kernel_initializer='uniform', activation='relu')) # 500 neurons
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, epochs=150, batch_size=10,  verbose=2) # 150 epoch, 10 batch size, verbose = 2
    if(args.save):
        model.save("Model-%s"%(datetime.now().strftime("%d%b%Y-%H-%M-%S")))
else:
    print(type(args.filepath))
    if(args.filepath):
        model = keras.models.load_model(str(args.filepath))
    else:
        model = keras.models.load_model("Default")
# evaluate the model
scores = model.evaluate(X, y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(X)    # predicting Y only using X
# evaluate the keras model 
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
print("*******************")
print("*******************")


secret_key = funcitions.toBinary("OLA")
neurons = model.weights[0][0].numpy()
Ti = funcitions.get_Ti(len(neurons),len(secret_key))
pseudo_random_sequence = funcitions.get_pseudorandom_sequence(Ti)
watermarked_neurons = funcitions.watermarkSS(original_neurons=neurons, key=secret_key ,Ti=Ti, sequence=pseudo_random_sequence)
decoded_watermark = funcitions.decodeSS(watermarked_neurons, Ti=Ti, sequence= pseudo_random_sequence)
print("DECODING")
casted_weights = []
print("Tamaño--"+str(size(model.weights)))
for i in range(0,len(model.weights)):
    #print("Tamaño[i]"+str(size(model.weights[i]))+"------Tamaño[i][0]"+str(size(model.weights[i][0])))
    #print("\t\t\t"+str(model.weights[i][0]))
    casted_weights = model.weights[i].numpy()

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
print("*******************")
print("*******************")
"""
print(len(model.weights))

print(model.weights[0][0].numpy())


for i in model.weights:
    print(type(i))

"""

for bit in decoded_watermark:
    print(chr(int(bit, 2)))


"""
print("*******************")
print(model.weights)
print("*******************")
for layer in model.layers:
    print(len(layer.get_weights()[0]))
    print(len(layer.get_weights()[1]))

print("*******************")
print(model.summary())
"""