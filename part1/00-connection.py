"""
Подключение к SQLite 3
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("ЗДЕСЬ БУДУТ НАШИ КОМАНДЫ")

