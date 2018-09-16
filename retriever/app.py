import os
import json

import redis

from urllib.parse import urlparse

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TweetListener(StreamListener): 
    def __init__(self):
        self.tweets = []
        self.redis = redis.StrictRedis.from_url(os.environ['URL_REDIS'])
        self.redis.flushall()

    def post(self, data):
        print('tweet-recieved. current-count: {}'.format(len(self.tweets)))
        self.tweets.append(data)

    def on_data(self, data):
        response = json.loads(data)
        self.post(response)
        return True

    def on_error(self, status):
        print(status)
        return False

def main():    
    consumer_key = os.environ['API_KEY_TWITTER_CONSUMER']
    consumer_secret = os.environ['API_SECRET_TWITTER_CONSUMER']

    access_key = os.environ['API_KEY_TWITTER_ACCESS_TOKEN']
    access_secret = os.environ['API_SECRET_TWITTER_ACCESS_TOKEN']

    listener = TweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    stream = Stream(auth, listener)

#    print(os.environ['KEYWORD_FILTER'])

    if os.environ.get('KEYWORD_FILTER') != None:
        stream.filter(track = os.environ['KEYWORD_FILTER'], async = True)
    if os.environ.get('LOCATION_FILTER') != None:
        stream.filter(locations = os.environ['LOCATION_FILTER'].split(','), async = True)

    while True:
        if len(listener.tweets) > 0:
#            print('tweets-stored. current-count: ', end='')
#             print(listener.tweets)
            listener.redis.lpush('queue:tweet', listener.tweets)
            listener.tweets = []

if __name__ == "__main__":
    main()
