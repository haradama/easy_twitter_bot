#coding: utf-8

import twitter
from settings import *

auth = twitter.OAuth(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    token=ACCESS_TOKEN,
    token_secret=ACCESS_TOKEN_SECRET
)

t = twitter.Twitter(auth=auth)

msg = "Hello World"
t.statuses.update(status=msg)
