from query_processor import preprocess_text, find_similar_movies
from db.db_routes import get_data_of_name

def get_films(query: str):
    proc_query = preprocess_text(query)
    film_names = find_similar_movies(proc_query)
    results = []
    for name in film_names:
        results.append(get_data_of_name(name)[0])
    return results

if __name__ == '__main__':
    res = get_films("быстрая езда по франции полиция и такси")
    print(res)