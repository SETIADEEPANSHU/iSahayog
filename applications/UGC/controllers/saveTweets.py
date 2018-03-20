#Twitter Rest API to fetch tweets
import tweepy
from tweepy import AppAuthHandler
import sys
import jsonpickle
import os
from datetime import date,timedelta
jp=local_import('json_parsing')
"""
consumer key, consumer secret, access token, access secret.
"""
ckey='gEsaZXKihn1D9pxhhHO27cCU1'
csecret='VJktYs030UXBrsOWsMjLZYklhYDFbav8cSgaXv6iix1c889oGE'
atoken='2724150318-MatzLw3eytypGmF1cinrBERRQ6PjdcYEjpZ8q1h'
asecret='F3EyeKHyZOANiyPWVBdlchB4wnzrtsmX428ycx4mxLRwf'
auth = AppAuthHandler(ckey, csecret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

searchQuery = 'TeamAtulya'
maxTweets = 10000000
tweetsPerQry = 100
fName = os.path.join(request.folder,'private','data.txt')
sinceId = None
times=date.today()-timedelta(0)  #Since when tweets need to be fetched.
print times
max_id = -1L
tweetCount = 0
#print("Downloading max {0} tweets".format(maxTweets))
while tweetCount < maxTweets:
    with open(fName, 'w') as f:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,until=times)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId,until=times)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),until=times)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId,until=times)
            if not new_tweets:
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
                jp.db=db
                jp.json_par(fName)
            tweetCount += len(new_tweets)
            #print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            #print("some error : " + str(e))
            break
