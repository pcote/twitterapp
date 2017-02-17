import unittest
from unittest.mock import MagicMock
from view import app
import model
import json

class TwitterAppTestCase(unittest.TestCase):
    def setUp(self):
        self.single_handle = "chicken_b"
        self.multiple_handles = "chicken_b BlenderNation".split()
        self.max_tweets = 25


    def get_json(self, res):
        raw_data = res.data
        string_data = raw_data.decode()
        json_ob = json.loads(string_data)
        return json_ob


    def testGetTweets(self):
        with app.test_client() as client:
            url = "/tweets?tweethandle={}&maxtweets={}"
            url = url.format(self.single_handle, self.max_tweets)
            res = client.get(url)

            # check for 200 status code.
            self.assertTrue("200" in res.status)

            # check to make sure there are tweet results
            msg = "There should be non-null results for json data"
            json_data = self.get_json(res)
            self.assertIsNotNone(json_data, msg)
            self.assertIn("tweets", json_data)

            # check to make sure tweets are a non-empty list.
            tweets = json_data["tweets"]
            tweet_count = len(tweets)
            self.assertTrue(tweet_count > 0)
            self.assertTrue(tweet_count == 25)

            # make sure all the screen names are coming up the same user
            screen_names = [tweet.get("screen_name") for tweet in tweets]
            all_same_user = all(sn == "chicken_b" for sn in screen_names)
            self.assertTrue(all_same_user, "The user should be the same for all tweets")


    def testGetMultipleUserTweets(self):
        with app.test_client() as client:
            # compose the url and url args together.
            handles = ["tweethandle={}".format(h)
                       for h in self.multiple_handles]
            handle_url_arg = "&".join(handles)
            url = "/tweets?{}&maxtweets={}".format(handle_url_arg, self.max_tweets)
            print("url for testGetMultipleUserTweets: {}".format(url))

            print("URL USED: {}".format(url))

            # make the request
            res = client.get(url)

            # check for 200 status code.
            self.assertTrue("200" in res.status)

            # check to make sure there are tweet results
            msg = "There should be non-null results for json data"
            json_data = self.get_json(res)
            self.assertIsNotNone(json_data, msg)
            self.assertIn("tweets", json_data)

            # check to make sure tweets are a non-empty list.
            tweets = json_data["tweets"]
            tweet_count = len(tweets)
            self.assertTrue(tweet_count > 0)
            self.assertTrue(tweet_count == 50)


            # make sure all the screen names are coming up from the test list of users
            screen_names = [tweet.get("screen_name") for tweet in tweets]
            for screen_name in screen_names:
                if screen_name not in self.multiple_handles:
                    self.fail("Screen name: {} should not be in this list of tweets".format(screen_name))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()