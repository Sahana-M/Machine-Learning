import tweepy
from textblob import TextBlob
consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret key'
access_token = 'your access token'
access_token_secret = 'your access token secret key'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Modi')
c=0
f=0
count=0
for tweets in public_tweets:
    print(tweets.text)
    count= count+1
    analysis = TextBlob(tweets.text)
    c = c + analysis.polarity
    f = f + analysis.subjectivity
    print(analysis.polarity)
    print("\n")
c = c/count
f = f/count
print("\nfor ",count , " tweets")
print("\nAverage polarity is :", c)
print("\nAverage subjectivity is :", f)
