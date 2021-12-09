import re
import nltk.corpus
#nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

def process_text(txt):
    text = txt.lower()
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    stop = stopwords.words('english')
    text = " ".join([word for word in text.split() if word not in (stop)])
    lemmatizer = WordNetLemmatizer()
    ltext = ""
    for word in text.split():
        ltext = ltext + lemmatizer.lemmatize(word) + " "
    return ltext.strip()