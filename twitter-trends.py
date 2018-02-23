
# coding: utf-8

# In[26]:


import tweepy
consumer_key = "NWZTZ8EaBC70nvBf8Fs5JpajJ"
consumer_secret = "6g4MsdI0C9XkmgaveHeAu74C8bcOeHwakpp1rPcsmWIQzT2DXK"
access_token = "2781754464-98TamoYx6If0rY2TWYvuQtD0rN9AFYjtV0vRLZt"
access_token_secret = "Szi3WFcvr4PCQyvakRSSaZRCed402DHoCnDzIBueTpnWg"


# In[27]:


# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 


# In[28]:


# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print tweet.text


# In[34]:


# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = raw_input("enter the trendname :")
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print tweet.user.screen_name,"Tweeted:",tweet._json
    
with open('/Users/o_fadairo/Desktop/data.txt', 'w') as outfile:  
    json.dump(data, outfile)


# In[33]:


# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = raw_input("enter the hashtag :")
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print tweet.user.screen_name,"Tweeted:",tweet._json


# In[19]:


import json
 
with open('/Users/o_fadairo/Desktop/tweettrend.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print
    file.close()
   


# In[24]:


import json
 
with open('/Users/o_fadairo/Desktop/tweettrend.json', 'r') as f:
    print f.read()
    file.close()


# In[43]:


from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("/Users/o_fadairo/Downloads/config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["2781754464-98TamoYx6If0rY2TWYvuQtD0rN9AFYjtV0vRLZt"], config["Szi3WFcvr4PCQyvakRSSaZRCed402DHoCnDzIBueTpnWg"], config["NWZTZ8EaBC70nvBf8Fs5JpajJ"], config["6g4MsdI0C9XkmgaveHeAu74C8bcOeHwakpp1rPcsmWIQzT2DXK"]))


#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------
results = twitter.trends.place(_id = 23424975)



# In[47]:


from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("/Users/o_fadairo/Downloads/config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------
results = twitter.trends.place(_id = 23424975)

print "UK Trends"

for location in results:
	for trend in location["trends"]:
		print " - %s" % trend["name"]

