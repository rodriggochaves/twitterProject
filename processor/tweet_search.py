from TwitterSearch import *
import unicodedata
# import re
import sys
import datetime

def getTweets(keywords):
	
	# let's set a limit to 1000 tweets
	limit_count = 1000

	# pega o input e transformar em um array de strings
	keywords = keywords.split(" ")

	try:
	    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	    tso.set_keywords(keywords) # let's define all words we would like to have a look for
	    tso.set_language('pt') # we want to see German tweets only
	    tso.set_count(100) # please dear Mr Twitter, only give us 100 results per page
	    tso.set_include_entities(False) # and don't give us all those entity information
	    # tso.setGeocode(-23.516394,-46.63554,1000,km=True)#I want only posts near Sao Paulo
	    # tso.setUntil(datetime.date(2014, 01, 26))

	    ts = TwitterSearch(
			consumer_key = 'VqUEyEu7lXO5z5lWqoTkYOUmZ',
			consumer_secret = 'aiGUuiCwWNrYherJ5USuPkeZi3WMdCJj0ZsIGtWSHlZgPeqpmI',
			access_token = '490611801-3ygNslO3ZvKXsGm1wZA1AdIwKO858jAsa66orMbd',
			access_token_secret = 'NZKkVwOYnz5BR1rf34PLHuODDnYlIaf52fbNBcMuUvU7b'
		)

	    for tweet in ts.search_tweets_iterable(tso): # this is where the fun actually starts :)
	        print( 'at %s' %   tweet['created_at'], tweet['text'])


	        date = tweet['created_at']
	        info = tweet['text'] + " " + date
	        data2Save = unicodedata.normalize('NFKD', info).encode('utf-8','ignore')

	        saveFile = open('tweets.txt', 'a')
	        saveFile.write(data2Save)
	        saveFile.write('\n')
	        saveFile.close()

	        limit_count -= 1
	        
	        if limit_count == 0:
				break


	except TwitterSearchException as e: # take care of all those ugly errors if there are some
	    print(e)

def hello():
	print "Jax is smoking"