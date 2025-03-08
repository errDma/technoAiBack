import sqlite3

def add_column(id: int, name: str, description: str, img_url: str):
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO movies (name, overview, img_url) 
        VALUES (?, ?, ?)
    ''', (name, description, img_url))

    conn.commit()
    conn.close()



def get_data_of_name(query):
    """
    Возвращает все строки из таблицы movies, где поле name равно query.

    :param query: Значение для поиска в поле name.
    :param db_path: Путь к базе данных SQLite.
    :return: Список словарей, где каждый словарь — это строка из таблицы.
    """
    print("SUKA BLUYAT\n\n")
    conn = sqlite3.connect("db/movies.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM movies WHERE name = ?", (query,))

    rows = cur.fetchall()

    result = [dict(row) for row in rows]

    conn.close()
    #print(f"result!: {result}")
    return result