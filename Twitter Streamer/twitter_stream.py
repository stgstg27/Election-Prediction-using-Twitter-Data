##################################
#####Twitter Streaming############
###Author : Saurabh Khandelwal####


import os
import pandas as pd
import sys
import json



"""
Loading twitter streamer library 
"""
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

	# @staticmethod
	def on_data(self,data):
		

		try:

			# print (type(data))
			# d = ast.literal_eval(data)
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
	twitterStream.filter(track=["Lok Sabha"],locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078])
	# twitterStream.filter()
