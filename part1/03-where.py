"""
Фильтрация данных
Условия - совпадение, диапазоны, вхождения, пустые значения
Комбинации - логические операторы
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT release_year, title, director
            FROM netflix
            WHERE director IS NULL
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
