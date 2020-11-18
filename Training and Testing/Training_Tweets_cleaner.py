import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import enchant
import pandas as pd

train = pd.read_csv('Labelled_tweets.tsv', header=0, delimiter="\t", \
               quoting=3 )

spell_dict = enchant.Dict('en-US')

fout = open('tweets_words.txt','w',encoding="utf8")
print("Please Wait...")
stop_words = set(stopwords.words("english"))
clean_train_tweets=[]
for i in range(0,len(train["tweet"])):
    sent=train["tweet"][i]
    sent=sent.lower()
    sen = re.sub("[^a-zA-Z]"," ", sent)
    if len(sen) > 0:
        clean=[]
        word=word_tokenize(sen)
        for w in word:
            if not w in stop_words and len(w)>2:
                if wordnet.synsets(w) and spell_dict.check(w):
                    clean.append(w)        
        clean_train_tweets.append(" ".join(clean))        
        fileData = str(clean_train_tweets[i]) + '\n'
        fout.write(fileData)

#print(clean_test_reviews)

fout.close()
print("Done!")
