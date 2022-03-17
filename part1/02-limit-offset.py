"""
Ограничение результатов и навигация
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM netflix LIMIT 10 OFFSET 10")

    for row in cursor.fetchall():
        print(row)
