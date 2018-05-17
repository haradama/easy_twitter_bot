# coding: utf-8

import twitter
from settings import *

auth = twitter.OAuth(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    token=ACCESS_TOKEN,
    token_secret=ACCESS_TOKEN_SECRET
)

t = twitter.Twitter(auth=auth)

count = 200
statuses = t.statuses.user_timeline(screen_name="XXXX", count=count)#user_id

with open("tweets.txt", "w") as f:
    for tweet in statuses:
        text = tweet["text"]
        f.write(text)
