from flask import Flask, session, redirect, request, render_template, url_for, jsonify, abort
import model

app = Flask(__name__)
app.secret_key="SetSecretKeyHere"


@app.route("/")
def index():
    return render_template("mainpage.html")


@app.route("/tweets", methods=["GET"])
def get_tweets():
    tweet_handles = request.args.getlist("tweethandle")
    max_tweets = request.args.get("maxtweets")
    max_tweets = int(max_tweets)

    tweet_list = []
    for tweet_handle in tweet_handles:
        tweets = model.get_tweets(tweet_handle, max_tweets)
        tweet_list.extend(tweets)

    results = dict(tweets=tweet_list)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
