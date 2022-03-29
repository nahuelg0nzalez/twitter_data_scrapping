from os import access
import pandas as pd
import tweepy
import configparser

#configuraciones

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

print(api_key)

#autenticacion

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


#######################


#extracción

public_tweets = api.home_timeline()

print(public_tweets[0].text) #muestra el último tweet en el feed

print(public_tweets[0].created_at) #hora de publicación del último tweet

print(public_tweets[0].user.screen_name) #nombre del usuario del último tweet

for tweet in public_tweets:
    print(tweet.text)


#############################


#creación de dataframe

columns = ['Fecha','Usuario','Tweet']
data = []

for tweet in public_tweets:
    data.append([tweet.created_at,tweet.user.screen_name,tweet.text])

df = pd.DataFrame(data,columns=columns)
print(df)


#crear un documento csv con el dataframe

df.to_csv('tweets.csv') 