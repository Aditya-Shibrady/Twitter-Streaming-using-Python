from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

consumer_key = '<insert>'
consumer_secret = '<insert>'
access_token = '<insert>'
access_secret = '<insert>'


class StdOutlistener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
            saveFile = open('twitter.json', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True

        except BaseException, e:
            print 'failed on data,', str(e)
            time.sleep(5)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutlistener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
    stream.filter(
        track=['@united'])