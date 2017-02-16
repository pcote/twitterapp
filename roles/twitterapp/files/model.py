from configparser import ConfigParser
import os
import twitter

this_directory = __file__.rsplit(os.path.sep, maxsplit=1)[0]
config_file_path = "{}{}config.ini".format(this_directory, os.path.sep)
cp = ConfigParser()
cp.read(config_file_path)

# TWITTER API SETUP
oauth_sec = cp["oauth"]
consumer_key = oauth_sec.get("consumer_key")
consumer_secret = oauth_sec.get("consumer_secret")
access_token_key = oauth_sec.get("access_token_key")
access_token_secret = oauth_sec.get("access_token_secret")
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)



def get_tweets(screen_name, num_tweets):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=num_tweets)
    timeline = [tweet.AsDict() for tweet in timeline]
    cleaned_up_list = []
    for entry in timeline:
        short_entry = dict()
        short_entry["id"] = entry["id"]
        short_entry["screen_name"] = entry["user"]["screen_name"]
        short_entry["message"] = entry["text"]
        short_entry["date"] = entry["created_at"]
        cleaned_up_list.append(short_entry)
    return cleaned_up_list