######Pre-Processing Tweets######
##Author: Saurabh Khandelwal#####





import pandas as pd
import re
import numpy as np
from nltk.stem.porter import *

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
