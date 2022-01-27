# first neural network with keras tutorial
import funcitions
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense




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

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=100, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(120, input_dim=8, activation='relu'))
model.add(Dense(12, activation='relu'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=2, batch_size=20)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

print("*******************")
print(model.weights)
print("*******************")
for layer in model.layers:
    print(len(layer.get_weights()[0]))
    print(len(layer.get_weights()[1]))

print("*******************")
print(model.summary())