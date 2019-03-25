import tweepy
import csv
import json

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_tweets(username):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	alltweets = []
	new_tweets = api.user_timeline(screen_name = username,count=100)
	alltweets.extend(new_tweets)

	with open('%s_tweets.txt' % username, 'w', encoding ='utf8') as f:
		for status in alltweets:
			f.write('\n**newTweet**\n')
			json.dump(status._json,f, ensure_ascii=False)
	
	outtweets = []
	for tweet in alltweets:
		if 'media' in tweet.entities:
			curr = [tweet.text.encode("utf-8"), tweet.created_at, tweet.favorite_count, tweet.retweet_count, len(tweet.entities['media'])]
		else:
			curr = [tweet.text.encode("utf-8"), tweet.created_at, tweet.favorite_count, tweet.retweet_count, 0]
		outtweets.append(curr)

	with open('%s_tweets.csv' % username, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["Text","created_at","Fav_Count", "Retweet_Count", "Images"])
		writer.writerows(outtweets)

	pass

if __name__ == '__main__':
	get_tweets('midasIIITD')