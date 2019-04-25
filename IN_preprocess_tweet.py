######Pre-Processing Tweets######
##Author: Saurabh Khandelwal#####





import pandas as pd
import re
import numpy as np
from nltk.stem.porter import *
import pickle
import os

def common_member(list1, list2):
	a_set = set(list1) 
	b_set = set(list2) 
	if (a_set & b_set): 
		return True 
	else: 
		return False

def load_file(file_name):
	df = pd.read_csv(file_name)
	# print (df.head())
	return df	

def remove_twiiter_handle(input_txt,pattern1, pattern2):
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

	nda_df = pd.read_csv('NDA.csv')
	upa_df = pd.read_csv('UPA.csv')
	abbr_df = pd.read_csv('Party and Abbreviation.csv')

	nda_1 = []
	upa_1 = []
	nda_1+=nda_df["Party Name"].tolist()
	upa_1+=upa_df["Party Name"].tolist()

	for i in range(len(abbr_df["Name"].tolist())):
		if abbr_df.iloc[i]["Name"] in nda_1:
			nda_1.append(abbr_df.iloc[i][1])

		if abbr_df.iloc[i]["Name"] in upa_1:
			upa_1.append(abbr_df.iloc[i][1])
		

	

	if common_member(nda_1,tweet.split()):
		ans = 1

	if common_member(upa_1,tweet.split()): 
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


	data_dict['NDA'] = list()
	data_dict['UPA'] = list()

	no_aspect_Term_found = 0
	num = 0
	for index,rows in pd_DF.iterrows():
		ct = check_tweet(rows['text'])
		print (num)
		num+=1
		if ct == 1:
			data_dict['NDA'].append(rows['text'])
		elif ct == 0:
			data_dict['UPA'].append(rows['text'])
		elif ct == 10:
			data_dict['NDA'].append(rows['text'])
			data_dict['UPA'].append(rows['text'])
		else:
			no_aspect_Term_found+=1


	with open('IN_data_dict.pickle', 'wb') as handle:
		pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

	
	print ("Currently unused tweets are ", no_aspect_Term_found)
	return data_dict,no_aspect_Term_found


def predict(data):
	score = dict()
	for key, value in data.iteritems() :
		print (key)
		score[key] = 0 
		for i in range(len(value)):
			score[key]+=(TextBlob(value[i]).sentiment.polarity)

	for i,value in score.iteritems():
		print (i,  " : ", value)



if __name__=="__main__":
	file_name = " tweet_lok_sabha.csv"
	df = load_file(file_name)
	
	print ("Number of tweets = ",len(df))
	num = 0
	
	print ("Removing Twitter Handle......")
	for index, rows in df.iterrows():
		rows['text'] = remove_twiiter_handle(rows['text'],"@[\w]*")
		num+=1

	text_column = "text"
	print ("removing excess characters")
	df = remove_characters(df,text_column)

	print ("Tokenizing tweet......")
	tokenized_tweet = tokenization(df,text_column)
	print ("Stemming Tweet.........")
	tokenized_tweet = stemming(tokenized_tweet)

	print("Saving the tokenized sentence")
	with open('IN_tokenized_tweet.pkl', 'wb') as f:
		pickle.dump(tokenized_tweet, f)

	print ("Saving the file to pre_process_Data.csv file")
	df.to_csv('IN_pre_process_Data.csv')

	print ("Diffrentiating terms based on the sentence")
	data_dict,no_aspect_Term_found = aspect_term_extraction(df,tokenized_tweet)

	predict(data_dict)