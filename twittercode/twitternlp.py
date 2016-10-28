import tweepy
import nltk

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

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text)
	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

