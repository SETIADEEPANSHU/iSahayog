import json
from gluon import *
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import jsonParsing

"""
consumer key, consumer secret, access token, access secret.
"""
ckey = "rt6NTjQJY1kXgL3rc2QcozXqO"
csecret = "9RvsWVDKb0HOoVGOknF1te2gi52poIpj2zvH5jBmmGb1pGo4Jw"
atoken = "294606786-dfOlNoeKJUEAYmWhzX98Ai51sJONMs3NbZZhXgk7"
asecret = "nzmhXj1vc4gYChRB6vFCqznsE0aWvIbIaBO8XaHcSWj38"


class listener(StreamListener):
    def on_data(self, data):
        try:
            x=os.path.join(current.request.folder, 'private', 'data.txt')
            with open(x, 'w') as outfile:
                json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=True, separators=(',', ': '))
            outfile.close()
            texts=jsonParsing.json_par(x)
            return texts
        except BaseException as e:
            #print "Error in data:"
            return False

    def on_error(self, status):
        #print status
        return True


def fetchTweets():
    l = listener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth, listener())
    stream.filter(track=['IndiaKaIdeaABC'], async=False)
