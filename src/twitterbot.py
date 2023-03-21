#twitterbot.py
import os
import tweepy as tw
import config

def init():

    #public
    consumer_key=config.consumer_key
    consumer_secret=config.consumer_secret
    acces_token=config.acces_token
    acces_token_secret=config.acces_token_secret

    auth=tw.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(acces_token,acces_token_secret)
    global api
    api=tw.API(auth, wait_on_rate_limit=True)

    #private
    consumer_keyz=config.consumer_keyz
    consumer_secretz=config.consumer_secretz
    acces_tokenz=config.acces_tokenz
    acces_token_secretz=config.acces_token_secretz

    authz=tw.OAuthHandler(consumer_keyz,consumer_secretz)
    authz.set_access_token(acces_tokenz,acces_token_secretz)
    global apiz
    apiz=tw.API(authz, wait_on_rate_limit=True)


def twitter(message):
    hashtag=config.hashtag
    message=message+hashtag
    api.update_status(message)

def twitterz(message):
    hashtag=config.hashtag
    message=message+hashtag
    apiz.update_status(message)