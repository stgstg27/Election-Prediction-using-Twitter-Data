######Pre-Processing Tweets######
##Author: Saurabh Khandelwal#####





import pandas as pd
import re
import numpy as np
import nltk

# import matplotlib.pyplot as plt

# import seaborn as sns

# import warning
import os


def load_file(file_name):
	df = pd.read_csv(file_name)
	# print (df.head())
	return df	

def remove_pattern(input_txt,pattern):
	r = re.findall(pattern,input_txt)
	print (type(r))
	for pat in r:
		input_txt = re.sub(pat,'',input_txt) 

if __name__=="__main__":
	file_name = "election_day_tweets.csv"
	df = load_file(file_name)
	print (df['text'].iloc[397599]) 

	df['text'].iloc[397599] = remove_pattern(df['text'].iloc[397599],"@[\w]*")
	print (df['text'].iloc[397599]) 
