#! python3

# Script for retrieving random tweet corpus through API
import tweepy, pandas as pd, csv, os

#get an authentication from Twitter

consumerKey = [redacted]
consumerSecret = [redacted]
accessToken = [redacted]
accessSecret = [redacted]
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
    for i in range(15):
        for tweet in getTweets(searchParam):
                writer.writerow([tweet.user.screen_name, tweet.text, tweet.user.location])
        print('One batch loaded!')
        
#with open('/Users/joaopedropadua/Desktop/' + searchParam + '.csv', 'r') as file:
names = ['User Name', 'Text', 'Location']
df = pd.read_csv('/Users/joaopedropadua/Desktop/' + searchParam + '.csv', names=names)
    #df = create_df(file, ['User Name', 'Text', 'Location'])
    
print(df.head)

with open('/Users/joaopedropadua/Desktop/covid19.txt', 'w') as file:
    text_base = [cell for cell in df['Text']]
    text = ' '.join(text_base)
    file.write(text)
# print(len(getTweets('Bolsonaro')))
