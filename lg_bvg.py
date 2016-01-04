#!/usr/bin/env python3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

import settings


bvg_accounts = ['232867314', '234688983', '234689386']
bvg_people = ['Yesica', 'Yesi', 'Ines', 'Nico', 'André', 'René', 'Chris', 'Petra', 'Klaus', 'Sabine', 'Dirk', 'Feierabend']


class BVGListener(StreamListener):

    def on_status(self, status):
        # check if tweet is either a retweet or a reply and drop it if so
        if not (hasattr(status, 'retweeted_status') or status.text.startswith('@')):
            print("New tweet: {}".format(status.text))
            # check if tweet is of actual value :-)
            if not any(name in status.text for name in bvg_people):
                print("→ RT")
                lg_bvg.retweet(status.id)
            else:
                print("→ dropped")

    def on_error(self, status_code):
        print("Error: {}".format(status_code))


if __name__ == '__main__':
    bvg = BVGListener()
    auth = OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)

    lg_bvg = API(auth)

    stream = Stream(auth, bvg)
    stream.filter(follow=bvg_accounts)
