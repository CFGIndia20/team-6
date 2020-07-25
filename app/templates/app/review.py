import cgi
form = cgi.FieldStorage()
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
def extract_features(word_list):
    return dict([(word, True) for word in word_list])
if __name__=='__main__':
   positive_fileids = movie_reviews.fileids('pos')
   negative_fileids = movie_reviews.fileids('neg')

features_positive = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in positive_fileids]
features_negative = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in negative_fileids]

threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

features_train = features_positive[:threshold_positive]+features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:]+features_negative[threshold_negative:]

classifier = NaiveBayesClassifier.train(features_train)

#input_reviews = [
#    "Started off as the greatest experiences of all time,great help",
#    "I loved the help offered.",
#    "Took too long to help,of no help",
#    "Did not like the service offered",
#    "Nice overall experience!",
#    "I will recommend everyone to actively participate in this!"
#]
review = form.getfirst("review", "0")

print("Predictions: ")

#for review in input_reviews:
#    print("\nReview:", review)
#    probdist = classifier.prob_classify(extract_features(review.split()))
#    pred_sentiment = probdist.max()
#print("Predictions: ")

#for review in input_reviews:
#    print("\nReview:", review)
     probdist = classifier.prob_classify(extract_features(review.split()))
     pred_sentiment = probdist.max()
#    print("Predicted sentiment: ", pred_sentiment)
#    print("Probability: ", round(probdist.prob(pred_sentiment), 2))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
#print "<p>%s</p>" % form  #uncomment this line if you want 
#to see what does form hashes look like 
print "<p>%s</p>" %pred_sentiment
print "<p>%s</p>" %probdist.prob(pred_sentiment)
print "<p>%s</p>" % input_text
print "</body>"
print "</html>"