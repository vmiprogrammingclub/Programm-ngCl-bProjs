from tweepy import OAuthHandler
import re

def __init__(self):
		# keys and tokens from the Twitter Dev Console
		consumer_key = 'ug9L2xYZIRL1Cf2kk1hkhGS3M'
		consumer_secret = 'sgveGUrGVNw3PA4e1OgYuRd32AM8zpkHzBT83NwkiNF5mTE74y'
		access_token = '2588243761-SUlzN6sXFNI4QvUeTiWooYX7AxR3tPZe796iYwI'
		access_token_secret = 'M9eIJcHE3m7sTfT83s6gHCYGpE6OMApMvqCh90WJGWxkE'
		self.auth = OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(self.auth)

def get_all_words(self, tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split())

def get_sentiment(self, tweet):
	clean_tweet = self.get_all_words(tweet)
	## my code
	##
	analysis = TextBlob(clean_tweet)
	# set sentiment
	if analysis.sentiment.polarity > 0:
		 return 'positive'
	elif analysis.sentiment.polarity == 0:
		 return 'neutral'
	else:
		 return 'negative'

def get_list_tweets(self, query, count = 1000):
	'''
	Main function to fetch tweets and parse them.
	'''
	# empty list to store parsed tweets
	tweets = []
	try:
		 # call twitter api to fetch tweets
		 fetch_tweets = self.api.search(q = query, count = count)
		 # parsing tweets one by one
		 for tweet in fetch_tweets:
				# empty dictionary to store required params of a tweet
				parsed_tweet = {}
				# saving text of tweet
				parsed_tweet['text'] = tweet.text
				# saving sentiment of tweet
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

				# adding parsed tweet to tweets list
				if tweet.retweet_count > 0:
					# if tweet has retweets, ensure that it is added to tweets only once
					if parsed_tweet not in tweets:
						 tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
		 # return parsed tweets
		 return tweets

	except tweepy.TweepError as e:
		 # print error (if any)
		 print("Error : " + str(e))


def main():
	# creating object of TwitterClient Class
	# api = TwitterClient()
	# calling function to get tweets
	tweets = self.get_tweets(query = '@wendys', count = 200)
	# picking positive tweets from tweets
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	# percentage of positive tweets
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	# picking negative tweets from tweets
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	# percentage of negative tweets 
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	# percentage of neutral tweets
	print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
	# printing first 5 positive tweets
	print("\n\nPositive tweets:")
	for tweet in ptweets[:10]:
		print(tweet['text'])
	# printing first 5 negative tweets
	print("\n\nNegative tweets:")
	for tweet in ntweets[:10]:
		print(tweet['text'])

if __name__ == "__main__":
	# calling main function
	main()