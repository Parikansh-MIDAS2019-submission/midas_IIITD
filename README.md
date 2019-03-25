## MIDAS_IIITD 2019 Summer Intern Task Submission
# This account and repo created only for this task. Original profile :
# github.com/parimatrix
This task has two parts:
### Tweet Fetcher
A python script to fetch tweets using tweepy and then save relevant information from the entire Tweet Object.
It stores the following details for each tweet:

● The text of the tweet.

● Date and time of the tweet.

● The number of favorites/likes.

● The number of retweets.

● Number of Images present in Tweet. If no image returns None.


### NLP Problem: Suggestion Mining from Text
Used __fasttext__ library and __Naive Bayes__ Classifier to classify the text input, whether it cocntains a suggestion or not.

The first subtask is for Same Domain Testing Data and the second subtask is for Cross Domain Testing Data

Cross Domain performance can be improved by combining datasets from different domains and then training on that combined set, and then that stronger classifier can be used to predict for any text input of any domain.
