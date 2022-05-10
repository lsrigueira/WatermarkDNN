# first neural network with keras tutorial
from statistics import mode
import funcitions
from numpy import loadtxt, size
from keras.models import Sequential
from keras.layers import Dense
from typing import Sequence
import funcitions
import argparse   

print(funcitions.toBinary("secre_key"))

"""
Code toreverse
n = int('0b110100001100101011011000110110001101111', 2)
binascii.unhexlify('%x' % n)
"""

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

model = Sequential()
# model.add(Dense(1000, input_dim=8, init='uniform', activation='relu')) # 1000 neurons
# model.add(Dense(100, init='uniform', activation='tanh')) # 100 neurons with tanh activation function
model.add(Dense(500, kernel_initializer='uniform', activation='relu')) # 500 neurons

model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid')) # 1 output neuron
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10,  verbose=2) # 150 epoch, 10 batch size, verbose = 2

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
for i in range(0,len(model.weights)):
    print(size(model.weights[i]))


model.set_weights(model.weights)

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