import os
import tweepy
 
cunsumer_key = os.environ['AK']
cunsumer_secret = os.environ['AS']
access_token = os.environ['AT']
access_token_secret = os.environ['ATS']
 
# API連携用のコード
auth = tweepy.OAuth1UserHandler(cunsumer_key, cunsumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)