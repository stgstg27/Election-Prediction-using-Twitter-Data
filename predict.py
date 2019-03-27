###Prediction for election based on twitter data########
####### Author : Saurabh Khandelwal ####################

import keras
import pickle

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.models import load_model

import os


def load_sentiment_model(filename):

	print ("Loading Model .....")
	curr_dirr = os.getcwd()
	curr_dirr+="/Models"
	print (curr_dirr)

	model = load_model(os.path.join(curr_dirr, filename))

	return model


def load_data(filename):

	print ("Loading data dictionary")
	with open(filename,"rb") as input_file:
		dataset = pickle.load(input_file)
	return dataset
	


def visualize():
	pass


def predict(data, model):
	for key, value in data.iteritems() :
		print (key)
		print (len(value))
		print (model.predict(value[0]))
if __name__ == '__main__':
	print ("################################## Prediction Start #################################")
	print (" load_sentiment_model................................................................")
	model = load_sentiment_model('weights-improvement-05-0.87.hdf5')
	data = load_data("data_dict.pickle")
	predict(data,model)


