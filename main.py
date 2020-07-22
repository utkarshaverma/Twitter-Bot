import tweepy
import random
from time import sleep
from credentials import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler("a7IYYQC1QwWzjQH9QA2zKC0Eg", 
    "ooDMylUtP0TM0ZBMUciXsQ7XxNI2wthlkIQS2KnS9lKjMEOCDA")
auth.set_access_token("1285930487156862976-2Cu6Gho0R7GcO91OFuXmiD5SFgR5co", 
    "PADxquKoY1RfV16nuaORayykD5QVQZvsktzSe6IzJq2zZ")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


#entering new tweets
my_file=open('sample.txt','r')
#read sample text from sample.txt and tweet a line from the text
file_lines=my_file.readlines()
my_file.close()
# choose random line from text to tweet.
status = random.choice(file_lines) 
try:
    print(status)
    if status != '\n':
        api.update_status(status)
    else:
        pass
except tweepy.TweepError as e:
    print(e.reason)
sleep(5)

#finding tweets based on user query and liking and retweeting the tweets.
query=input("Enter hashtag to filter tweets   :  ")
#print(query)
query='#'+query

for tweet in tweepy.Cursor(api.search, q=query, tweet_mode = 'extended').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        print(tweet.full_text)

        # Like tweets as they are found
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                print('Liked the tweet')
            except Exception as e:
                print(e)

        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                print('Retweeted the tweet')
            except Exception as e:
                print(e)
        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
