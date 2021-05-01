import sys
import tweepy
import config as cfg
import pandas as pd
import re

class StreamListener(tweepy.StreamListener):
    def __init__(self):
    	# Make sure to initialize parent class
    	super(StreamListener, self).__init__()

    	# tweets: List of dictionaries
    	#	[tweet]: String - tweet
    	#	[score]: Int - numeric sentiment for the tweet
    	self.tweets = []

    	# num_tweets: Int - Number of tweets handled
    	self.num_tweets = 0

    	# aggregate_score: Float - the sum of scores of all tweets handled
    	self.aggregate_score = 0.0

    	# current_score: Float - The current sentiment of all tweets aggregated
    	self.current_score = 0.0

    def on_status(self, status):
        tweet = self.format_tweet(status.text)
        print(tweet)
        score = 1

        # Create dictionary from the handled tweet
        tweet_dict = {}
        tweet_dict["tweet"] = tweet
        tweet_dict["score"] = score

        # Append to tweets field
        self.tweets.append(tweet_dict)

        # Increment num_tweets
        self.num_tweets += 1

        # Increment aggregate score
        self.aggregate_score += score

        # Recalculate current score
        self.current_score = self.aggregate_score / self.num_tweets

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def format_tweet(self, tweet):
    	# Remove all text that contains "http" or "" or "RT"
    	tokens = tweet.split(" ")
    	tokens = [s for s in tokens if "http" not in s and "@" not in s and "RT" not in s]
    	tweet_f = " ".join(str(s) for s in tokens)

    	# Format all text as lowercase
    	tweet_f = tweet_f.lower()

    	# Remove all non alphabet characters
    	tweet_f = re.sub('[^a-zA-z0-9\s]','',tweet_f)

    	return(tweet_f) 

def get_api():
	auth = tweepy.OAuthHandler(cfg.consumer_key, cfg.consumer_secret)
	auth.set_access_token(cfg.access_key, cfg.access_secret)
	api = tweepy.API(auth)
	return(api)

def main(phrase):
	print(phrase)

	api = get_api()

	stream_listener = StreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
	try:
		stream.filter(track=[phrase])
	except KeyboardInterrupt:
		pass

	# Create CSV file of all the tweets handled and their corresponding scores
	df = pd.DataFrame(stream_listener.tweets)
	df.to_csv(phrase + ".csv", index = False)


if __name__ == "__main__":
	phrase = sys.argv[1]
	main(phrase)