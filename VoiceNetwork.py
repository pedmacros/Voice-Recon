from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import csv
from keras.models import Sequential

from keras.layers import Dense

# from keras.utils import np_utils
# from sklearn import metrics


X = []
Y = []
dataset = np.loadtxt('/content/drive/My Drive/collab/data.csv', delimiter=',')
X = dataset[:, 0:-1]
Y = dataset[:, -1]
print('Will this work? -> ', X.shape)
print('Will this work? -> ', Y.shape)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=22)

print('I dont know what to say anymore ->', X.shape)
print('Shape of train ->', x_train.shape)
print('Shape of test ->', x_test.shape)

model = Sequential()

model.add(Dense(300, input_dim=67584, activation='relu'))
model.add(Dense(33791, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)