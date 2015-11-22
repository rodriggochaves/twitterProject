import nltk
import unicodedata

class Classifier():

	def __init__(self, goodWords, badWords):
		pos_tweets = self.arrayWithMood(goodWords, "positive")
		neg_tweets = self.arrayWithMood(badWords, "negative")
		
		tweets = []
		# isolate every >= 3 word associated with a feeling
		for (words, sentiment) in pos_tweets + neg_tweets:
		    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
		    tweets.append((words_filtered, sentiment))

		# all words are filtered and prepared to be used by the traning set creator
		self.word_features = self.get_word_features(self.get_words_in_tweets(tweets))

		# from featured word, creates a traning set applying thats
		# contains the presence or not frow all features
		training_set = nltk.classify.apply_features(self.extract_features, tweets)
		
		# The Naive Bayes classifier uses the prior probability of each label 
		# which is the frequency of each label in the training set, and the 
		# contribution from each feature. In our case, the frequency of each 
		# label is the same for 'positive' and 'negative'. The word 'amazing'
		# appears in 1 of 5 of the positive tweets and none of the negative 
		# tweets. This means that the likelihood (probabilidade) of the 
		# 'positive' label will 
		# be multiplied by 0.2 when this word is seen as part of the input.
		self.classifier = nltk.NaiveBayesClassifier.train(training_set)

	
	def arrayWithMood(self, array, feeling):
		arrayWithFeeling = []
		for word in array:
			arrayWithFeeling.append((word, feeling))
		return arrayWithFeeling

	def get_words_in_tweets(self, tweets):
	    all_words = []
	    for (words, sentiment) in tweets:
	      	all_words.extend(words)
	    return all_words

	def get_word_features(self, wordlist):
	    wordlist = nltk.FreqDist(wordlist)
	    word_features = wordlist.keys()
	    return word_features

	def extract_features(self, document):
	    document_words = set(document)
	    features = {}
	    for word in self.word_features:
	        features['contains(%s)' % word] = (word in document_words)
	    return features
		