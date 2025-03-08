import pandas as pd
import string
import pymorphy3
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

morph = pymorphy3.MorphAnalyzer()
stop_words = set(stopwords.words('russian'))



def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [morph.parse(word)[0].normal_form for word in words if word not in stop_words]
    return ' '.join(words)

