from numpy import loadtxt
from keras.models import load_model

model = load_model('my_model.h5')
model.summary()
dataset = loadtxt('/content/drive/My Drive/collab/guess.csv',delimiter=',')

X = dataset.reshape(1,24000)
print('dataset is')
print(X.shape)
print(type(X))
Y = model.predict_classes(X)
# show the inputs and predicted outputs
for i in range(len(X)):
	print("X=%s, Predicted=%s" % (X[i], Y[i]))
