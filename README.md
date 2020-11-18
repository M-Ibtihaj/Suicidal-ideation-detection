# Suicidal-ideation-detection
To categorize tweets according to the severity level of suicidal intentions expressed in tweets’ text.

## Description
This work aims to categorize tweets according to the severity level of suicidal intentions expressed in tweets’ text.

## Dataset
Tweets texts having word suicide in them
	
## Preprocessing
In preprocessing following operations are done:
- Repetitive neighbor words removal
- Repetitive characters removal and spelling correction
- Negative words replacement
- Stop words removal
- Symbols and numbers removal
- Manual cleaning of some parts causing processing overhead

## Labels
- **0**
> Tweet content is not suicidal
- **1**
> Tweet content is nearly related to suicidal ideation
- **2**
> Tweet content indicating a user potentially committing suicide

## Folders and files
  - ### Tweets Data Retrieval
       - **Tweets_Data_Retrieval:** Retrieving suicidal tweets  
  - ### Training and Testing
       - **antonyms_list:** File containing words and their antonyms for negative words replacement
       - **prepro_lib:** Contains files for preprocessing operations
       - **Data_preprocessor:** Preprocessing of data
       - **Training_Tweets_cleaner:** Symbols and other minor cleaning
       - **Training_Testing:** Training and testing the model
  - ### Datset
       - **Raw_suicide_tweets:** Tweets' texts
       - **Labelled_tweets:** Training data
       - **test:** Test data
       - **tweets_words:** Words extracted from tweets data after preprocessing

## Requirements
- Python 3.6 or above
- Tweepy
- NLTK
- Yaml
- Enchant
- Scikit Learn
- Pandas
- Numpy

## Platform
Python
