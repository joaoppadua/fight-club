#! python3

# Script for retrieving random tweet corpus through API
import json
import tweepy

#get an authentication from Twitter

consumerKey = '2TDhqQpqDJ5vElZT5RwmmUUvR'
consumerSecret = '1FvO85YI8AfaQ86kOmCxLvf2A8aaxCJozWnZKGzA712aClzI6n'
accessToken = '184757106-XpRQiy0dk9YTLuC8QAuX5WROYJSYikIvgzSHXP7L'
accessSecret = 'YhOdhds60M6v48DJZxxT88zJaQGvrnfmIkNKkn9g2seSU'
searchParam = input('Enter search parameter: ')

#Access Twitter API

def getTweets(param):
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    api = tweepy.API(auth)
    tweets = api.search(param)
    return tweets


#Save tweets to a file (.txt) 

with open('C:\\Users\\João Pedro\\Desktop\\Twitter - {}.txt'.format(searchParam), 'a', errors='replace') as f:
    for tweet in getTweets(searchParam):
        f.write(tweet.user.name + ' ' + tweet.text + '\n')



# print(len(getTweets('Bolsonaro')))