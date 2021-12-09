# Multilabel classification of restaurnat reviews
When ever a customer rates a restaurant or hotel they review it baed on the following aspects:
1. Food
2. Service
3. Ambience
4. Price

In this project we will create a Multilabel classification model using Logistic Regression with OneVsRest classifier to detect the aspect of an Intent. I created a dataset for this project which is avaiable [here]().

The model works good for food, service and ambience, but needs some tuning for detecting price related reviews. All the reviews has been taken from Google using my scraper which is avaiable [here](https://github.com/saisyam/reviews-scraper).
