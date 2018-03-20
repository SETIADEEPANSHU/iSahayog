import tweepy
from gluon import *
#VARIABLES CONTAINING USER CREDITENTIALS
consumer_key='gEsaZXKihn1D9pxhhHO27cCU1'
consumer_secret='VJktYs030UXBrsOWsMjLZYklhYDFbav8cSgaXv6iix1c889oGE'
access_token='2724150318-MatzLw3eytypGmF1cinrBERRQ6PjdcYEjpZ8q1h'
access_secret='F3EyeKHyZOANiyPWVBdlchB4wnzrtsmX428ycx4mxLRwf'

''' 	get_api function is for getting the access authorization from
	twitter api.
'''

def get_api():
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_secret)
	return tweepy.API(auth)
	
'''	main function is here to post the tweet on the timeline of
	user of which access token is used in the get_api function
'''

def posts(tweet,im_path):
	api=get_api()
	if im_path!='':
		status=api.update_with_media(im_path,status=tweet)
	else:
		status=api.update_status(status=tweet)
