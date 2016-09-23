'''9/14/2016
   python twitter bot testing!!!
   '''

import tweepy
import random
import os

def main():

    with open("secrets.txt") as f:
        secrets = f.readlines()
    f.close()

    #set authorization variables
    CONSUMER_KEY = secrets[0].strip('\n')
    CONSUMER_SECRET = secrets[1].strip('\n')
    ACCESS_TOKEN = secrets[2].strip('\n')
    ACCESS_SECRET = secrets[3].strip('\n')

    #tweepy needs that info
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    #now we are connected to tweepy, time to make some tweets
    tweetlist = ["Woah! A computer made this tweet!",
                 "This is a randomly generated tweet!",
                 "We're learning about the twitter API!"]

    #atlist = ["@weareicwc","@bethdellea", "@meataphor"]

    contentNum = random.randint(0, len(tweetlist)-1)
    #atNum = random.randint(0, len(atlist)-1)
    tweet = "@meatahpor did this break things?"  #atlist[atNum] + " " + tweetlist[contentNum]  #random text plus random directed user, for funsies
    api.update_status(tweet)

main()
