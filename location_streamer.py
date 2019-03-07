from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


#Streams and processes live tweets
class TwitterStreamer():
    def stream_tweets(self, filename, loc_range):
        #Twitter auth  and connecting to Twitter Streaming API
        listener =StdOutListener(filename)
        
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        stream.filter(locations=loc_range)

#Basic listener  that just prints received tweets
class StdOutListener(StreamListener):
    def __init__(self, filename):
        self.filename = filename

    #takes data streamed from the StreamListener
    def on_data(self, data):
        try:
            print(data)
            with open(self.filename, 'a') as tf:
                tf.write(data + ',')
            return True
        except BaseException as e:
            print("Error on data: %s " % str(e))
        return True

    
    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    loc_range =  [-180,-90,180,90]
    filename = "tweets2.json"

    twitterStreamer = TwitterStreamer()
    twitterStreamer.stream_tweets(filename, loc_range)