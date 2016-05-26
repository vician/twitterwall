import tweepy

ckey = "_YOUR_CKEY_"
csecret = "_YOUR_CSECRET_"
atoken = "_YOUR_ATOKEN_"
asecret = "_YOUR_ASECRET_"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
         'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

cricTweet = tweepy.Cursor(api.search, q='#installfest').items(10)

for tweet in cricTweet:
    #print tweet.created_at, tweet.text, tweet.lang
    #print
    print tweet
    print 
