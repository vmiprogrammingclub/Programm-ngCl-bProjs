#Authors: Aaron Causey, Zach Harris, Kathleen Yates, Robert DuPont
from tkinter import *
import re
import tweepy
from tweepy import OAuthHandler
from tkinter import scrolledtext
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import praw
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                   client_id='', client_secret="",
                     username='', password='')
import twython
#submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')

from pprint import pprint
import pandas as pd
import nltk
nltk.download('vader_lexicon')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')
import requests, urllib                     # Importing Libraries..
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

APP_ACCESS_TOKEN = "***********************"  # Access_Token: Generate your acess token by urself..
BASE_URL = 'https://api.instagram.com/v1/'


window = Tk()

window.title("Sentimental Analysis GUI")

window.geometry('600x400')





subRedditkeyphraseBox = Entry(window, width=10,)
subRedditkeyphraseBox.grid(column=2, row=2)

lb2 = Label(window, text="Enter Subreddit:")
lb2.grid(column=1, row=2)


InstaBox = Entry(window, width=10,)
InstaBox.grid(column=2, row=3)
lb3 = Label(window, text="Enter Instagram Handle:")
lb3.grid(column=1, row=3)




#ScrollText


#CheckBox Variables
RedditVar = IntVar()
    #Reddit Variables

TwitterVar = IntVar()
InstagramVar = IntVar()



#Twitter
def clicked():
    scrollTextwindow = Tk()

    scrollTextwindow.title("CommandLine")

    scrollTextwindow.geometry('1000x800')
    scrollText = scrolledtext.ScrolledText(scrollTextwindow, width=800, height=600)

    scrollText.grid(column=0, row=5)
    if TwitterVar.get() == 1:
        scrollText.insert(INSERT, "Twitter Stats:")




        keyphrase = keyphrasetxtBox.get()


        # ###############################################################################################

        #                                           Class Def

        # ###############################################################################################

        class TwitterClient(object):


            def __init__(self):

                # keys and tokens from the Twitter Dev Console

                consumer_key = ''

                consumer_secret = ''

                access_token = ''

                access_token_secret = ''

                self.auth = OAuthHandler(consumer_key, consumer_secret)

                self.auth.set_access_token(access_token, access_token_secret)

                self.api = tweepy.API(self.auth)

            def clean_tweet(self, tweet):

                '''

                Utility function to clean tweet text by removing links, special characters

                using simple regex statements.

                '''

                return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split())

            def get_tweet_sentiment(self, tweet):

                '''

                Utility function to classify sentiment of passed tweet

                using textblob's sentiment method

                '''

                # create TextBlob object of passed tweet text

                analysis = TextBlob(self.clean_tweet(tweet))

                # set sentiment

                if analysis.sentiment.polarity > 0:

                    return 'positive'

                elif analysis.sentiment.polarity == 0:

                    return 'neutral'

                else:

                    return 'negative'

            def get_tweets(self, query, count= 200):

                '''

                Main function to fetch tweets and parse them.

                '''

                # empty list to store parsed tweets

                tweets = []

                try:

                    # call twitter api to fetch tweets

                    fetched_tweets = self.api.search(q=query, count=count)

                    # parsing tweets one by one

                    for tweet in fetched_tweets:

                        # empty dictionary to store required params of a tweet

                        parsed_tweet = {}

                        # saving text of tweet

                        parsed_tweet['text'] = tweet.text

                        # saving sentiment of tweet

                        parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                        # appending parsed tweet to tweets list

                        if tweet.retweet_count > 0:

                            # if tweet has retweets, ensure that it is appended only once

                            if parsed_tweet not in tweets:
                                tweets.append(parsed_tweet)

                        else:

                            tweets.append(parsed_tweet)

                    # return parsed tweets

                    return tweets


                except tweepy.TweepError as e:

                    # print error (if any)

                    print("Error : " + str(e))

        # ###############################################################################################

        #                                           Main

        # ###############################################################################################

        def main():

            # creating object of TwitterClient Class

            api = TwitterClient()

            # calling function to get tweets

            tweets = api.get_tweets(query= keyphrase, count=200)

            # picking positive tweets from tweets


            ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

            # percentage of positive tweets

            if tweets.count != 0:
                positivePercent = str(100 * len(ptweets) / len(tweets))
                positivePercentN = (100 * len(ptweets) / len(tweets))

                scrollText.insert(INSERT, "\nPositive Percentage of Tweets: " + positivePercent)



            # picking negative tweets from tweets

                ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

            # percentage of negative tweets

                negativePercent = str(100 * len(ntweets) / len(tweets))
                negativePercentN = (100 * len(ntweets) / len(tweets))

                scrollText.insert(INSERT, "\nNegative Percentage of Tweets: " + negativePercent)

            # percentage of neutral tweets
                neutralPercent = str(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
                neutralPercentN = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))

                scrollText.insert(INSERT, "\nNeutral Percentage of Tweets: " + neutralPercent)
                scrollText.insert(INSERT, "\n")

            # Graph for users


                objects = ('Postive', 'Negative', 'Neutral')
                y_pos = np.arange(len(objects))
                performance = [positivePercentN, negativePercentN, neutralPercentN]

                plt.bar(y_pos, performance, align='center', alpha=0.5)
                plt.xticks(y_pos, objects)
                plt.ylabel('Percentage')
                plt.title('Twitter Post Analysis')

                plt.show()





            else:
                scrollText.insert(INSERT, "\nNo current Tweets on this subject")


            # printing first 5 positive tweets

            # print("\n\nPositive tweets:")

                #  for tweet in ptweets[:10]:
            #      print(tweet['text'])

            # printing first 5 negative tweets

            #   print("\n\nNegative tweets:")

                #  for tweet in ntweets[:10]:
            #      print(tweet['text'])


        if __name__ == "__main__":
            # calling main function

            main()

    if RedditVar.get() == 1:
        scrollText.insert(INSERT, "\nReddit Stats:")

        keyphrase = keyphrasetxtBox.get()
        Redditkeyphrase = subRedditkeyphraseBox.get()

        all = reddit.subreddit(Redditkeyphrase)

        redditPostTotal = 0.0
        redditPositiveTotal = 0.0
        redditNegativeTotal = 0.0
        redditNeutralTotal = 0.0

        for i in all.search(keyphrase, limit=5):
            link = "https://www.reddit.com" + i.permalink
            #scrollText.insert(INSERT, "\nLink: " + link)
            submission = reddit.submission(url=link)
            for comment in submission.comments:
                try:
                    string = comment.body
                    string = re.sub(u"(\u2018|\u2019|\u201d|\u201c|\u2014)", "'", string)
                    emoji_pattern = re.compile("["
                                               u"\U0001F600-\U0001F64F"  # emoticons
                                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                               "]+", flags=re.UNICODE)
                    string = emoji_pattern.sub(r'', string)
                    #scrollText.insert(INSERT, "\n" + string)
                    from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

                    sia = SIA()
                    results = []

                    pol_score = sia.polarity_scores(string)
                    pol_score['Reddit Post'] = string
                    results.append(pol_score)
                    compoundScore = str(pol_score['compound'])
                    #scrollText.insert(INSERT,  "\n" + compoundScore + "\n")
                    redditPostTotal += 1

                    if (pol_score['compound'] > .2):
                        redditPositiveTotal +=1
                    elif (pol_score['compound'] < .2):
                        redditNegativeTotal+=1
                    else:
                        redditNeutralTotal+=1



                except:
                    continue

        positivePercent = (redditPositiveTotal / redditPostTotal) * 100
        positivePercentS = str(positivePercent)
        negativePercent = (redditNegativeTotal / redditPostTotal) * 100
        negativePercentS = str(negativePercent)
        neutralPercent = (redditNeutralTotal / redditPostTotal) * 100
        neutralPercentS = str(neutralPercent)

        scrollText.insert(INSERT, "\nPercentage of Positive Posts: " + positivePercentS)
        scrollText.insert(INSERT, "\nPercentage of Negative Posts: " + negativePercentS)
        scrollText.insert(INSERT, "\nPercentage of Neutral Posts: " + neutralPercentS)

        objects = ('Postive', 'Negative', 'Neutral')
        y_pos = np.arange(len(objects))
        performance = [positivePercent, negativePercent, neutralPercent]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Percentage')
        plt.title('Reddit Post Analysis')

        plt.show()

    if InstagramVar.get() == 1:
        def get_user_id(insta_username):  # Defining function to get User_ID by passing username ..
            request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
            scrollText.insert(INSERT, (colored('GET request url : %s\n', 'blue') % (request_url)))
            user_info = requests.get(request_url).json()

            if user_info['meta']['code'] == 200:
                if len(user_info['data']):
                    return user_info['data'][0]['id']
                else:
                    return None
            else:
                scrollText.insert(INSERT, (colored('Status code other than 200 received!\n', 'red')))
                exit()
        def get_comment_list(insta_username):  # Defining the Function ............
            media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
            request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (
            media_id, APP_ACCESS_TOKEN)  # passing the end points and media id along with access token ..
            scrollText.insert(INSERT, (colored('GET request url : %s\n', 'blue') % (request_url)))
            comment_list = requests.get(request_url).json()

            if comment_list['meta']['code'] == 200:  # checking the status code .....
                if len(comment_list['data']):
                    position = 1
                    scrollText.insert(INSERT, (colored("List of people who commented on Your Recent post", 'blue')))
                    for _ in range(len(comment_list['data'])):
                        if comment_list['data'][position - 1]['text']:
                            scrollText.insert(INSERT,(colored(comment_list['data'][position - 1]['from']['username'], 'magenta') + colored(
                                ' said: ', 'magenta') + colored(comment_list['data'][position - 1]['text'],
                                                                'blue')))  # Json Parsing ..printing the comments ..
                            position = position + 1
                        else:
                            scrollText.insert(INSERT,(colored('No one had commented on Your post!\n', 'red')))
                else:
                    scrollText.insert(INSERT, (colored("There is no Comments on User's Recent post.\n", 'red')))
            else:
                scrollText.insert(INSERT, (colored('Status code other than 200 recieved.\n', 'red')))
        def get_post_id(keyphrase):
            user_id = get_user_id(keyphrase)  # Capturing the user id ......
            if user_id == None:  # checking in case post exists or not .......
                scrollText.insert(INSERT, (colored('InstaUser of this Username does not exist!\n', 'red')))
                exit()
            request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
            scrollText.insert(INSERT, (colored('GET request url : %s\n', 'blue') % (request_url)))
            user_media = requests.get(request_url).json()  # Fetching json data ........

            if user_media['meta']['code'] == 200:  # checking the status code .......
                if len(user_media['data']):
                    return user_media['data'][0]['id']
                else:
                    scrollText.insert(INSERT, (colored('There is no recent post of the user!\n', 'red')))
                    exit()
            else:
                scrollText.insert(INSERT, (colored('Status code other than 200 received!\n', 'red')))
                exit()


    instagramHandle = "@"
    instagramHandle += InstaBox.get()
    get_comment_list(instagramHandle)





# Buttons

lbl = Label(window, text="Enter your key phrase")

lbl.grid(column=0, row=0)

keyphrasetxtBox = Entry(window, width=10)

keyphrasetxtBox.grid(column=1, row=0)

btn = Button(window, text="Search", command=clicked)

btn.grid(column=2, row=0)





#Check Box
Checkbutton(window, text="Twitter", variable=TwitterVar).grid(row=1, sticky=W)
Checkbutton(window, text="Reddit", variable=RedditVar).grid(row=2, sticky=W)
Checkbutton(window, text="Instagram", variable=InstagramVar).grid(row=3, sticky=W)



window.mainloop()
