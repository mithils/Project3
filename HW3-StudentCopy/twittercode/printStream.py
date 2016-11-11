import tweepy
import json

# Unique code from Twitter
access_token = "791818305707335681-dclJMCNmxy8o2AewAYF151lezepQVsR"
access_token_secret = "JqIAWuCOKdw5b3FMzOkWzY2A07BAbNBonuyFATrMIH8UQ"
consumer_key = "Gad8GyO2Bp2c6ZBQYRp3dVBvs"
consumer_secret = "hIOqWR3AMm2CwDBbg4BbMwRFBCv2lcKJirMU2cET7veL6AHHzK"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


