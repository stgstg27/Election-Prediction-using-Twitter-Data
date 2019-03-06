######Pre-Processing Tweets######
##Author: Saurabh Khandelwal#####





import pandas as pd
import re
import numpy as np
from nltk.stem.porter import *
import pickle

import pickle

your_data = {'foo': 'bar'}

# Store data (serialize)
with open('filename.pickle', 'wb') as handle:
    pickle.dump(your_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

# import matplotlib.pyplot as plt

# import seaborn as sns

# import warning
import os


def load_file(file_name):
	df = pd.read_csv(file_name)
	# print (df.head())
	return df	

def remove_twiiter_handle(input_txt,pattern):
	r = re.findall(pattern,input_txt)
	for pat in r:
		input_txt = re.sub(pat,'',input_txt) 
	
	return input_txt

def remove_characters(pd_DF,column_name):
	"""
	Removing Punctuations, Numbers, and Special Characters
	"""
	pd_DF[column_name] = pd_DF[column_name].str.replace("[^a-zA-Z#]", " ")

	return pd_DF 

def remove_short_words(pd_DF,column_name):
	"""
	Removing words like oh,hmm etc
	"""

	pd_DF[column_name] = pd_DF[column_name].apply(lambda x : ' '.join([w for w in x.split() if len(w)>3]))

	return pd_DF

def tokenization(pd_DF,column_name):
	"""
	tokenize all the cleaned tweets in our dataset. Tokens are individual terms or words, and tokenization is the process of splitting a string of text into tokens
	"""
	tokenized_tweet = pd_DF[column_name].apply(lambda x: x.split())
	print (tokenized_tweet.head())

	return tokenized_tweet

def stemming(tokenized_tweet):
	"""
	"""
	stemmer = PorterStemmer()

	tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
	tokenized_tweet.head()

	return tokenized_tweet

def check_tweet(tweet):
	ans = -1

	if "Donald" in tweet or "Trump" in tweet or "Mike" in tweet or "Pence" in tweet or "Republican" in tweet:
		ans = 1

	if "Hillary" in tweet or "Clinton" in tweet or "Tim" in tweet or "Kaine" in tweet or "democrats" in tweet or "Democratic" in tweet : 
		if ans == 1:
			ans = 10
		else:
			ans = 0


	return ans




def aspect_term_extraction(pd_DF, tokenized_tweet):
	"""
	Currently Aspect term extracted are for Donald, Trump, Hillary, Clinton,Mike, Pence, Tim Kaine, Democratic,Republican,democrats

	"""

	data_dict = dict()


	data_dict['Republican'] = list()
	data_dict['Democratic'] = list()

	no_aspect_Term_found = 0
	for index,rows in pd_DF.iterrows():
		ct = check_tweet(rows['text'])
		
		if ct == 1:
			data_dict['Republican'].append(rows['text'])
		elif ct == 0:
			data_dict['Democratic'].append(rows['text'])
		elif ct == 10:
			data_dict['Republican'].append(rows['text'])
			data_dict['Democratic'].append(rows['text'])
		else:
			no_aspect_Term_found+=1


	with open('data_dict.pickle', 'wb') as handle:
		pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

	return data_dict,no_aspect_Term_found




if __name__=="__main__":
	file_name = "election_day_tweets.csv"
	df = load_file(file_name)
	
	print ("Number of tweets = ",len(df))
	num = 0
	
	print ("Removing Twitter Handle......")
	for index, rows in df.iterrows():
		rows['text'] = remove_twiiter_handle(rows['text'],"@[\w]*")
		print (num)
		num+=1

	text_column = "text"
	print ("removing excess characters")
	df = remove_characters(df,text_column)

	print ("Tokenizing tweet......")
	tokenized_tweet = tokenization(df,text_column)
	print ("Stemming Tweet.........")
	tokenized_tweet = stemming(tokenized_tweet)

	print("Saving the tokenized sentence")
	with open('tokenized_tweet.pkl', 'wb') as f:
		pickle.dump(tokenized_tweet, f)

	print ("Saving the file to pre_process_Data.csv file")
	df.to_csv('pre_process_Data.csv')

	print ("Diffrentiating terms based on the sentence")
	data_dict,no_aspect_Term_found = aspect_term_extraction(df,tokenized_tweet)
