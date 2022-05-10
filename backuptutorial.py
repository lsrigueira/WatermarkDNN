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
"""
model = Sequential()
model.add(Dense(120, input_dim=8, activation='relu'))
model.add(Dense(12, activation='relu'))
model.fit(X, y, epochs=2, batch_size=20)
"""
model = Sequential()
# model.add(Dense(1000, input_dim=8, init='uniform', activation='relu')) # 1000 neurons
# model.add(Dense(100, init='uniform', activation='tanh')) # 100 neurons with tanh activation function
model.add(Dense(500, kernel_initializer='uniform', activation='relu')) # 500 neurons
# 95.41% accuracy with 500 neurons
# 86.99% accuracy with 100 neurons
# 85.2% accuracy with 50 neurons
# 81.38% accuracy with 10 neurons
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid')) # 1 output neuron
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10,  verbose=2) # 150 epoch, 10 batch size, verbose = 2


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