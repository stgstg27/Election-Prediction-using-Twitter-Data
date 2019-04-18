###Prediction for election based on twitter data########
####### Author : Saurabh Khandelwal ####################

import pickle
from textblob import TextBlob
import os
import gensim

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
	


def visualize(data, model):
	plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
	


def predict(data):
	score = dict()
	for key, value in data.iteritems() :
		print (key)
		score[key] = 0 
		for i in range(len(value)):
			score[key]+=(TextBlob(value[i]).sentiment.polarity)

	for i,value in score.iteritems():
		print (i,  " : ", value)


if __name__ == '__main__':
	print ("################################## Prediction Start #################################")
	print (" load_sentiment_model from textblob................................................................")
	data = load_data("data_dict.pickle")
	predict(data)


