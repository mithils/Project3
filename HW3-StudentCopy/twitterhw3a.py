# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy
import os
import sys
# Unique code from Twitter
access_token = "791818305707335681-dclJMCNmxy8o2AewAYF151lezepQVsR"
access_token_secret = "JqIAWuCOKdw5b3FMzOkWzY2A07BAbNBonuyFATrMIH8UQ"
consumer_key = "Gad8GyO2Bp2c6ZBQYRp3dVBvs"
consumer_secret = "hIOqWR3AMm2CwDBbg4BbMwRFBCv2lcKJirMU2cET7veL6AHHzK"
# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
picture = 'media/Harbaugh.jpg'
tags = '@CoachJim4UM #UMSI-206 #Proj3' #Contains tweet message and tags
status = api.update_with_media(picture, status=tags)
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")
