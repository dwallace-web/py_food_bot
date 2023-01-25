import config
import time
import tweepy
from tweepy.api import pagination
from tweepy.client import Response
import csv
from datetime import date

# date
current_date = str(date.today())


client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
auth = tweepy.OAuthHandler(consumer_key=config.API_KEY,
                           consumer_secret=config.API_KEY_SECRET)
api = tweepy.API(auth)