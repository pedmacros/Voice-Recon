from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import csv
from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Flatten
# from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
# from keras.optimizers import Adam
# from keras.utils import np_utils
# from sklearn import metrics


X = []
Y = []
le = LabelEncoder()


def trainNetwork():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        rawData = list(reader)
    print("number of rows -> ",len(rawData))
    fft = []
    authors = []
    for recording in rawData:
        authors.append(recording[-1])
        fft.append(recording[:-1])
    print('Authors before labeling ->', authors)
    X = np.asarray(fft)
    le.fit(authors)
    print('Fit authors ->', le.classes_)
    Y = le.transform(authors)
    print('Outputs ->', Y)
    print('Type of X ->', type(X))

    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=22)

    input_shape = 67584


    print('Length of train ->',x_train)
    print('Length of test ->',len(x_test))


    model = Sequential()
