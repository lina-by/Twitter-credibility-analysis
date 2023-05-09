import pickle
from textblob import TextBlob
from textblob import Word
import os

from textblob.classifiers import NaiveBayesClassifier
# load the classifiers
with open(os.getcwd()+'/textual_analysis/toxic_classifier.pkl', 'rb') as fid:
    tox = pickle.load(fid)

# test : print(tox.classify("fuck you dumb bitch"))


def Violence(text):
    text = TextBlob(text)
    text= text.translate(to="en")
    s=0
    if tox.classify(text)=="toxic":
        s=1
    return s

# test : print("connasse", violence("connasse"))