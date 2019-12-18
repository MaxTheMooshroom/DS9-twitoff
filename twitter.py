"""Retrieve tweets, embedding, save into database"""

import basilica
import tweepy
from .models import DB, Tweet, User
from os import environ as VARS

TWITTER_AUTH = tweepy.OAuthHandler(VARS['TWITTER_CONSUMER_KEY'],
                                   VARS['TWITTER_CONSUMER_SECRET'])

TWITTER_AUTH.set_access_token(VARS['TWITTER_ACCESS_TOKEN'],
                              VARS['TWITTER_ACCESS_TOKEN_SECRET'])

TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(VARS['BASILICA_KEY'])

#to do - add functions later 
