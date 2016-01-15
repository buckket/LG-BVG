#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from sklearn.externals import joblib

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

import settings


bvg_accounts = ['232867314', '234688983', '234689386']


class BVGListener(StreamListener):

    def on_status(self, status):
        # check if tweet is either a retweet or a reply and drop it if so
        if not (hasattr(status, 'retweeted_status') or status.text.startswith('@')):
            print("New tweet: {}".format(status.text.encode('UTF-8')))
            # check if tweet is of actual value :-)
            predict = text_clf.predict([status.text.encode('UTF-8')])[0]
            if predict == 1:
                print("→ RT")
                lg_bvg.retweet(status.id)
            else:
                print("→ dropped")

    def on_error(self, status_code):
        print("Error: {}".format(status_code))


if __name__ == '__main__':
    text_clf = joblib.load('model/bvg_model.pkl')

    bvg = BVGListener()
    auth = OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)

    lg_bvg = API(auth)

    stream = Stream(auth, bvg)
    stream.filter(follow=bvg_accounts)
