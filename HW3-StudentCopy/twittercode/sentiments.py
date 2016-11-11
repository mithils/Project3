import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "791818305707335681-dclJMCNmxy8o2AewAYF151lezepQVsR"
access_token_secret = "JqIAWuCOKdw5b3FMzOkWzY2A07BAbNBonuyFATrMIH8UQ"
consumer_key = "Gad8GyO2Bp2c6ZBQYRp3dVBvs"
consumer_secret = "hIOqWR3AMm2CwDBbg4BbMwRFBCv2lcKJirMU2cET7veL6AHHzK"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" @netflix')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
