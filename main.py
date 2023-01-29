import config, requests, json
import tweepy
from datetime import date

auth = tweepy.OAuthHandler(consumer_key=config.API_KEY,
                           consumer_secret=config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

data = []

api.update_status("Food processor on the way")

def get_food_data():
    global data 
    res = requests.get('https://data.cityofchicago.org/resource/4ijn-s7e5.json')
    data = res.text
    print(len(data), " results" )

get_food_data()

# def get_food_fails():