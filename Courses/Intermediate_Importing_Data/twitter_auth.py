# 1640014718-ywUwnpfPENiOZLKjJkjRg1WbYISyIh13Vb6j38f (access token)
# 6iiqXDteEzBbl6LuYgJpQdNnv15KXdxOTcfoWfzY82MpO (access token secret)
# ej89OqxCl3vAYd7OPdCYKI45z (API consumer key)
# Yga9J9ODeXXLmIlMsmS3dqmQCMF3drABdI0nLmWbmfudn6Y9Z7 (API consumer secret)


import tweepy
import json

access_token = "1640014718-ywUwnpfPENiOZLKjJkjRg1WbYISyIh13Vb6j38f"
access_token_secret = "6iiqXDteEzBbl6LuYgJpQdNnv15KXdxOTcfoWfzY82MpO"
consumer_key = "ej89OqxCl3vAYd7OPdCYKI45z"
consumer_secret = "Yga9J9ODeXXLmIlMsmS3dqmQCMF3drABdI0nLmWbmfudn6Y9Z7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
