import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import enchant
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

spell_dict = enchant.Dict('en-US')
fin = open('tweets_words.txt','r',encoding="utf8")
train = pd.read_table('Labelled_tweets.tsv', header=0, \
                delimiter="\t", quoting=3)
test = pd.read_csv('test.tsv', header=0, delimiter="\t", \
               quoting=3 )
trainD = fin.read()
trainD = trainD.splitlines()
fin.close()

# Initialize the "CountVectorizer" object, which is scikit-learn's bag of words tool.
vectorizer = CountVectorizer(analyzer = "word")

# fit_transform
train_data_features = vectorizer.fit_transform(trainD)
# Numpy arrays
np.asarray(train_data_features)
##vocab = vectorizer.get_feature_names()
##print(vocab)
##Logistic Regression
classifier = LogisticRegression()
classifier.fit(train_data_features,train["category"])
##test data cleaning
stop_words = set(stopwords.words("english"))
clean_test_tweets=[]
for i in range(0,len(test["tweet"])):
    sent=test["tweet"][i]
    sent=sent.lower()
    sen = re.sub("[^a-zA-Z]"," ", sent)
    if len(sen) > 0:
        clean=[]
        word=word_tokenize(sen)
        for w in word:
            if not w in stop_words and len(w)>2:
                if wordnet.synsets(w) and spell_dict.check(w):
                    clean.append(w)
        clean_test_tweets.append(" ".join(clean))
            
test_data_features = vectorizer.transform(clean_test_tweets)
np.asarray(test_data_features)

##NB predictions
result=classifier.predict(test_data_features)
# Copy the results to a pandas dataframe
data={'id':test['id'],'Category':result}
output = pd.DataFrame(data)

output.to_csv('Result.csv', index=False, quoting=3)
print("Wrote results to Result.csv")

