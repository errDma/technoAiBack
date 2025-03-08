import pandas as pd
import numpy as np
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer

conn = sqlite3.connect('teach_data.db')
df = pd.read_sql('SELECT * FROM training_data', conn)
vectorizer = TfidfVectorizer(max_features=10000)
movie_vectors = vectorizer.fit_transform(df['description']).toarray()