##################################
#####Twitter Streaming############
###Author : Saurabh Khandelwal####


import os
import pandas as pd
import sys


"""
Loading twitter streamer library 
"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey = 'Please enter your key'
csecret = 'Please enter your key'
atoken = 'Please enter your key'
asecret = 'Please enter your key'

class listener(StreamListener):

	# @staticmethod
	def on_data(self,data):
		print (type(data))

		print (data)
		
		return True

	# @staticmethod
	def on_error(self,status):
		print (status)

	# def on_exception(self,temp):
	# 	print (temp)






if __name__ == '__main__':
	print ("Authorizing.....")
	auth = OAuthHandler(ckey,csecret)
	auth.set_access_token(atoken,asecret)
	typel = listener()
	print ("Streaming Tweets.....\n")
	twitterStream = Stream(auth, typel)
	print (twitterStream)
	twitterStream.filter(track=["Lok Sabha"])
