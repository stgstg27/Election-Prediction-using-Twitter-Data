##################################
#####Twitter Streaming############
###Author : Saurabh Khandelwal####


import os
import pandas as pd
import sys
import json
import csv


"""
Loading twitter streamer library 
"""
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from time import time

import ast


ckey = 'GzVdXYb5gst4jxyURsrTFr5h5'
csecret = '0cx9YobVWQxOTkP9lfOJ633UZAMTkS5Hepk3amItLmBzasPqlQ'
atoken = '1037785443113332738-ew5mL19tdUqH1WTESumINKjDtaXHwX'
asecret = '9zWoKeUSPjNQmDB5EML7fGkaX6JtkndoMt9Hg4nIgAUj6'


class listener(StreamListener):

	def on_data(self,data):
		

		try:
			yy  =json.dumps(data)
			print (yy)
			print (type(data))
			dataset = open("tweetDB.csv","a")
			dataset.write(data)
			dataset.write("\n")
			dataset.close()

			return True

		except BaseException,e :
			print ("Failed, please check your internet connectivity" , e)
			
	# @staticmethod
	def on_error(self,status):
		print (status)







if __name__ == '__main__':
	print ("Authorizing.....")
	auth = OAuthHandler(ckey,csecret)
	auth.set_access_token(atoken,asecret)

	typel = listener()
	print ("Streaming Tweets.....\n")
	twitterStream = Stream(auth, typel)
	# twitterStream.filter(track=["Lok Sabha"],locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078])
	
	api = tweepy.API(auth,wait_on_rate_limit=True)
	csvFile = open('IN_Tweets_17-4_25-4.csv', 'a')

	#Use csv writer
	csvWriter = csv.writer(csvFile)
	i = 0
	for tweet in tweepy.Cursor(api.search,
	                           q = "Lok Sabha",
	                           since = "2019-04-17",
	                           until = "2019-04-24",
	                           locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078],	
	                           lang = "en").items():

	    # Write a row to the CSV file. I use encode UTF-8
	    print (i)
	    i+=1
	    link = 1
	    if len(tweet._json["entities"]["urls"]) == 0:
	    	link = 0
	    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet._json['retweet_count'], tweet._json['retweeted'], tweet._json["user"]["followers_count"],link])

	    if i % 10 == 0:
			csvFile.close()
			print ("saved file, Number of tweets = ",i, "\n\n\n\n\n")
			csvFile = open('IN_Tweets_17-4_25-4.csv', 'a')

			#Use csv writer

			csvWriter = csv.writer(csvFile)


	    print tweet.created_at, tweet.text
	    
	csvFile.close()