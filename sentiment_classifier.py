######Sentiment Classifier ######
##Author: Saurabh Khandelwal#####


from keras.datasets import imdb
from keras.preprocessing import sequence
import numpy as np
import keras
import matplotlib.pyplot as plt
import os
print ("Loading data with vocab size = 5000............")
top_words = 5000
if not os.path.isfile('X_train.npy'):

	(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
	np.save('X_train',X_train)
	np.save('y_train',y_train)
	np.save('X_test',X_test)
	np.save('y_test',y_test)

else:
	X_train = np.load('X_train.npy')
	y_train = np.load('y_train.npy')
	X_test = np.load('X_test.npy')
	y_test = np.load('y_test.npy')

max_words = 500

print ("padding sequence ot max_words = 500.............")
X_train = sequence.pad_sequences(X_train, maxlen = max_words)
X_test = sequence.pad_sequences(X_test, maxlen = max_words)


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding

def model():

	print ("Creating Sequential Model................")
	model = Sequential()
	model.add(Embedding(top_words, 32, input_length = max_words))
	model.add(Conv1D(filters = 32, kernel_size = 3, padding = 'same', activation = 'relu'))
	model.add(MaxPooling1D(pool_size = 2))
	model.add(Flatten())
	model.add(Dense(250,activation = 'relu'))
	model.add(Dense(1,activation = 'sigmoid'))
	model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

	print (model.summary())

	return model

# Fit the model
filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
tb = keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=0, batch_size=32, write_graph=True,
									 write_grads=False, write_images=False, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None, embeddings_data=None, update_freq='epoch')
checkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor = 'val_loss', verbose = 1, save_best_only = False, save_weights_only = False, mode = 'auto', period = 1)
model = model()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs = 5, batch_size=128, verbose=2, callbacks = [checkpoint,tb])
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose = 1)
print("Accuracy: %.2f%%" % (scores[1]*100))







