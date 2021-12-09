import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import hamming_loss, accuracy_score

from cleanup import *
stop_words = set(stopwords.words('english'))

df = pd.read_csv("reviews.csv", encoding = "ISO-8859-1")
df = df.drop(['tokens'], axis=1)
df.head()

df['review'] = df['review'].map(lambda com : process_text(com))

X = df['review']
y = np.asarray(df[df.columns[1:]])

  
# splitting the data to training and testing data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


LogReg_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                ('clf', OneVsRestClassifier(LogisticRegression(solver='sag'), n_jobs=1)),
            ])
LogReg_pipeline.fit(X_train, y_train)

new_sentences = ["Friendly staff and great food but expensive"]
  
predicted_sentences = LogReg_pipeline.predict(new_sentences)
print(predicted_sentences)