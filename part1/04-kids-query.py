"""
Информацию по детским фильмам (G) за последние пять лет,
у которых проставлена дата добавления
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT title, release_year
            FROM netflix
            WHERE rating = 'G'
            AND release_year > 2016
            AND date_added IS NOT NULL
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
