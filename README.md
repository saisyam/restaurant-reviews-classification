# Multilabel classification of restaurnat reviews
When ever a customer rates a restaurant or hotel they review it baed on the following aspects:
1. Food
2. Service
3. Ambience
4. Price

In this project we will create a Multilabel classification model using Logistic Regression with OneVsRest classifier to detect the aspect of an Intent. I created a dataset for this project which is avaiable [here]().

The model works good for food, service and ambience, but needs some tuning for detecting price related reviews. All the reviews has been taken from Google using my scraper which is avaiable [here](https://github.com/saisyam/reviews-scraper).

Install the necessary packages from `requirements.txt`. Download `nltk` bundles using the following commands:

```
$ python3
Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> nltk.download('stopwords')
[nltk_data] Downloading package stopwords to
[nltk_data]     /home/saisyam/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
True
>>> nltk.download('wordnet')
[nltk_data] Downloading package wordnet to /home/saisyam/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
True
>>> 
```