'''testing fetching a list of users and displaying the description heads for each user selected
9/18/2016'''

import tweepy

def main():
    with open("secrets.txt") as f:
        secrets = f.readlines()
    f.close()

    CONSUMER_KEY = secrets[0].strip('\n')
    CONSUMER_SECRET = secrets[1].strip('\n')
    ACCESS_TOKEN = secrets[2].strip('\n')
    ACCESS_SECRET = secrets[3].strip('\n')

    #give tweepy the authorization info
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)


    #get a list of the representatives on the twitter verified us-congress list
    #it's our starting point, at least
    allRepList = tweepy.Cursor(api.list_members, "verified", "us-congress").items()
    printedCount = 0
    for user in allRepList:
        if printedCount < 15:
            print (user.screen_name)
            print (user.description)
            printedCount += 1
            #to keep the printout concise
    
main()

