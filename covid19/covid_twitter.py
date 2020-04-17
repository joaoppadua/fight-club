#! python3

# Script for retrieving random tweet corpus through API
import json, tweepy, pandas as pd, csv, os

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
    tweets = api.search(param, lang='en')
    return tweets

#def create_df(file, *col):
#    df = pd.read_csv(file, names=col, header=None)
#    return df

#Test
#data = [(tweet.user.screen_name, tweet.text, tweet.entities['hashtags'][0]['text'], tweet.user.location) for tweet in getTweets(searchParam)]
#print(data[:100])


#Save tweets to a file (.txt) 

with open('/Users/joaopedropadua/Desktop/' + searchParam + '.csv', 'a', newline='', errors='replace') as f:
    writer = csv.writer(f)
    for tweet in getTweets(searchParam):
            writer.writerow([tweet.user.screen_name, tweet.text, tweet.user.location])
        
with open('/Users/joaopedropadua/Desktop/' + searchParam + '.csv', 'r') as file:
    names = ['User Name', 'Text', 'Location']
    df = pd.read_csv(file, names=names)
    #df = create_df(file, ['User Name', 'Text', 'Location'])
    
print(df.head)


# print(len(getTweets('Bolsonaro')))