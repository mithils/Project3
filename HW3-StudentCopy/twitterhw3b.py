# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob
access_token = '791818305707335681-dclJMCNmxy8o2AewAYF151lezepQVsR'
access_token_secret= 'JqIAWuCOKdw5b3FMzOkWzY2A07BAbNBonuyFATrMIH8UQ'
consumer_key= 'Gad8GyO2Bp2c6ZBQYRp3dVBvs'
consumer_secret= 'hIOqWR3AMm2CwDBbg4BbMwRFBCv2lcKJirMU2cET7veL6AHHzK'
# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
term_of_choice = input('Enter term of choice:') 
public_tweets = api.search(term_of_choice) #Prints each tweet based on search term
list_subjectivity = []
list_polarity = []
for tweet in public_tweets: #Determines subjectivity and polarity of each tweet
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	list_subjectivity.append(analysis.sentiment.subjectivity)
	list_polarity.append(analysis.sentiment.polarity)
sum_subjectivity = sum(list_subjectivity)
sum_polarity = sum(list_polarity)
length_subjectivity = len(list_subjectivity)
length_polarity = len(list_polarity)
print("Average subjectivity is", sum_subjectivity/length_subjectivity)
print("Average polarity is", sum_polarity/length_polarity)
