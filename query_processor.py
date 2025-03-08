import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from preproces import preprocess_text
from data_proces import df, vectorizer, movie_vectors


def get_query_vector(query):
    return vectorizer.transform([query]).toarray()

def find_similar_movies(query, top_n=5):
    query_vector = get_query_vector(query)
    similarities = cosine_similarity(query_vector, movie_vectors)
    similar_indices = np.argsort(similarities[0])[::-1][:top_n]
    return df['name'].iloc[similar_indices].tolist()

if __name__ == "__main__":
    query = "случайный укус паука радиактивного"
    proc_query = preprocess_text(query)
    print(find_similar_movies(proc_query))