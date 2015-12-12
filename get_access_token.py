#!/usr/bin/env python3

import sys
import tweepy

import settings


def main():
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)

    print(auth.get_authorization_url())

    verifier = input("Verifier: ")
    auth.get_access_token(verifier)

    print("Access token: {}".format(auth.access_token))
    print("Access token secret: {}".format(auth.access_token_secret))


if __name__ == '__main__':
    sys.exit(main())
