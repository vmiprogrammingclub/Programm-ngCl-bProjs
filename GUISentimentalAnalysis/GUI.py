#Authors: Aaron Causey, Zach Harris, Robert Dupont, Kathleen Yates
from Tkinter import *

import re

import tweepy

from tweepy import OAuthHandler

from Tkinter import scrolledtext

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from textblob import TextBlob
import praw

def main():
    reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                       client_id='******', client_secret="******",
                         username='******', password='******')

    #submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')



    window = Tk()

    window.title("Sentimental Analysis GUI")

    window.geometry('600x400')





    subRedditkeyphraseBox = Entry(window, width=10,)

    lb2 = Label(window, text="Enter Subreddit:")
    lb2.grid(column=1, row=2)
    subRedditkeyphraseBox.grid(column=2, row=2)


    #ScrollText


    #CheckBox Variables
    RedditVar = IntVar()
        #Reddit Variables

    TwitterVar = IntVar()



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

                    consumer_key = '******'

                    consumer_secret = '******'

                    access_token = '************'

                    access_token_secret = '******'

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




                # printing first 5 negative tweets and positive

                    print("\n\nNegative tweets:")

                for tweet in ntweets[:10]:
                    print(tweet['text'])

                print("\n\nPositive tweets:")

                for tweet in ptweets[:10]:
                    print(tweet['text'])

            if __name__ == "__main__":
                # calling main function

                main()

        if RedditVar.get() == 1:
            scrollText.insert(INSERT, "\nReddit Stats:")

            keyphrase = keyphrasetxtBox.get()
            Redditkeyphrase = subRedditkeyphraseBox.get()

            all = reddit.subreddit(Redditkeyphrase)

            for i in all.search(keyphrase, limit=5):
                link = "https://www.reddit.com" + i.permalink
                scrollText.insert(INSERT, "\nLink: " +link)
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
                        scrollText.insert(INSERT, "\n" + string)
                    except:
                        continue


    # Buttons

    lbl = Label(window, text="Enter your key phrase")

    lbl.grid(column=0, row=0)

    keyphrasetxtBox = Entry(window, width=10)

    keyphrasetxtBox.grid(column=1, row=0)

    btn = Button(window, text="Search", command=clicked)

    btn.grid(column=2, row=0)





    ##ChecK BoX
    Checkbutton(window, text="Twitter", variable=TwitterVar).grid(row=1, sticky=W)
    Checkbutton(window, text="Reddit", variable=RedditVar).grid(row=2, sticky=W)


    window.mainloop()

    #positivePercent, positiveTweets

main()