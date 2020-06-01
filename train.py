from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import csv
from keras.models import Sequential
from keras.layers import Dense
import torch

# from keras.utils import np_utils
# from sklearn import metrics

le = LabelEncoder()
X = []
Y = []
dataset = np.loadtxt('/content/drive/My Drive/collab/datos.csv', delimiter=',')
X = dataset[:, 0:-1]
Y = dataset[:, -1]

print('Y before encoding ->', Y)
le.fit(Y)
Y = le.transform(Y)
print('Y after encoding ->', Y)
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=22)

print('Shape of train ->', x_train.shape)
print('Shape of test ->', x_test.shape)

model = Sequential()

model.add(Dense(8000, input_dim=24000, activation='relu'))
model.add(Dense(2000, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=150, batch_size=10)

_, accuracy = model.evaluate(X, Y)
print('Accuracy: %.2f' % (accuracy*100))

model.save('my_model.h5')