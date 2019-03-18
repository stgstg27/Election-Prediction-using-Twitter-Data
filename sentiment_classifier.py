######Sentiment Classifier ######
##Author: Saurabh Khandelwal#####


from keras.datasets import imdb
from keras.preprocessing import sequence
import numpy as np

import matplotlib.pyplot as plt

print ("Loading data with vocab size = 5000............")
top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)


max_words = 500

X_train = sequence.pad_Sequence(X_train, maxlen = max_words)
X_test = sequence.pad_Sequence(X_test, maxlen = max_words)


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding

def model():

	print ("Creating Sequential Model....")
	model = Sequential()
	model.add(Embedding(top_words, 32, input_length = max_words))
	model.add(Conv1D(filter = 32, kernel_size = 3, padding = 'same', activation = 'relu'))
	model.add(MaxPooling1D(pool_size = 2))
	model.add(Flatten())
	model.add(Dense(250,activation = 'relu'))
	model.add(Dense(1,activation = 'sigmoid'))
	model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

	print (model.summary())

	return model

# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs = 5, batch_size=128, verbose=2)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))







