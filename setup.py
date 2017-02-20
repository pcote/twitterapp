# setup.py
# Script for entering the configuration data for
# the Twitter API and the self-signed SSl certificate
import re
import json
from pprint import pprint

def make_json_file(twitter_info, ssl_info):
    with open("deployvarsdev.json", "rt") as f:
        json_ob = json.load(f)

    json_ob.update(twitter_info)
    json_ob.update(ssl_info)

    with open("deployvarsdev.json", "wt") as f:
        json.dump(json_ob, f, indent=0)





if __name__ == '__main__':
    header_msg = """
    #########################################
    # Setup configuration for twitterapp    #
    #########################################
    """
    print(header_msg)

    header_msg = """
    --- Enter the following information from your Twitter API account---
    --- Go to the link below if you haven't set that part up yet.    ---

    https://apps.twitter.com/
    """

    print(header_msg)
    twitter_info = dict()
    twitter_info["consumer_key"] = raw_input("Consumer Key: ")
    twitter_info["consumer_secret"] = raw_input("Consumer Secret: ")
    twitter_info["access_token_key"] = raw_input("Access Token Key: ")
    twitter_info["access_token_secret"] = raw_input("Access Token Secret: ")

    print("\n\nOkay.  Here is the twitter api info you've entered thus far...")
    for k, v in twitter_info.items():
        print("{:20}: {}".format(k, v))

    print("\n\nOkay.  Now we'll put in information the self-signed SSL certificate...\n\n")
    ssl_info = dict()
    ssl_info["certcity"] = raw_input("City: ")
    ssl_info["certstate"] = raw_input("State (2 character abbreviation): ")
    country = raw_input("Country: ")
    ssl_info["certcountry"] = country[:2] #BUGFIX: openssl dies if you feed it a country with more than 2 chars

    print("\n\nOkay.  Here is the Open SSL info entered for the SSL cert you will be creating...\n\n")
    for k, v in ssl_info.items():
        print("{:20}: {}".format(k, v))

    print("\n\nNow that that step is done, you may now create the configuration file used to setup twitterapp.")
    create_conf = raw_input("Are you ready to continue?  (Y/n): ")
    create_conf = create_conf.strip()

    patt = r"^y(es)?$"
    if re.match(patt, create_conf, re.IGNORECASE):
        print("\nokay lets do this!!!!\n")
        make_json_file(twitter_info, ssl_info)
    else:
        print("\nDon't want to continue?  No problem.  Come back later when you're ready to move forward.")
