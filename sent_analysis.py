from textblob import TextBlob
import sys, tweepy

#Your Twitter API Authentication Variables
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

auth = tweepy.OAuthHandler(consumer_secret=consumerSecret, consumer_key = consumerKey)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy. API(auth)

#Will evaluate the newest 100 tweets
print("This Senitment Analyzer will avaluate the newest 100 tweets based on your query and return the average Compound Score")
query = input("Enter query to evaluate: ")

tweets = api.search(query, count=100)

sent = 0
for tweet in tweets:
    blob = TextBlob(tweet.text)
    sent = sent + blob.sentiment.polarity
    
sent = sent/100
print("Average Comp Score across the hundred tweets:")
print(sent)
