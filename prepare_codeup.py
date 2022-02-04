import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import acquire_codeup


#acquire_codeup.get_blog


def basic_clean(x):
    #lowercase
    x = x.lower()
   
    #normalize unicode characters
    #normalize removes any inconsistencies in unicode character
    # .encode converts the resulting stirng to ascii character set, we ingore any errors in the conversions (we drop any non ascii characters)
    # .decode turn resulting bytes into string
    x = unicodedata.normalize('NFKD', x)\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')

    #replace anyting that is not a letter, number, whitespace or a single quote
    x = re.sub(r"[^a-z0-9'\s]", '', x)
    return x


def tokenize(x):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    x = tokenizer.tokenize(x , return_str = True)
    return x



def stem(x):
    ps = nltk.porter.PorterStemmer()

    stems = [ps.stem(word) for word in x.split()]
    aritcle_stemmed = ' '.join(stems)
    return aritcle_stemmed



def lemmatize(x):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in x.split()]

    article_lemmatized = ' '.join(lemmas)
    return article_lemmatized


def remove_stopwords(extra_words, exclude_words, x):
    # setting the list to english
    stopword_list = stopwords.words('english')

    stopword_list = [stopword_list.append(i) for i in extra_words]
    stopword_list = [stopword_list.remove(i) for i in exclude_words]

    words = x.split()
    filtered_words = [w for w in words if w not in stopword_list]

    article_without_stopwords = ' '.join(filtered_words)
    return article_without_stopwords