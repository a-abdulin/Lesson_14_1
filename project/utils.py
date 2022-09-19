import sqlite3


def select_execute(query):
    with sqlite3.connect("./netflix.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(query)
    return result.fetchall()


def movie_by_title(movie_title):
    query = f"SELECT title, country, release_year, description FROM netflix WHERE netflix.title= '{movie_title}'"
    result_data = select_execute(query)
    output = {}
    output["title"] = result_data[0][0]
    output["country"] = result_data[0][1]
    output["release_year"] = result_data[0][2]
    output["description"] = result_data[0][3]
    return output


def movie_by_year(year1, year2):
    query = f"SELECT title, release_year " \
            f"FROM netflix " \
            f"WHERE release_year BETWEEN {year1} and {year2}"
    result_data = select_execute(query)
    output_list = []
    output_dict = {}
    for row in result_data:
        output_dict["title"] = row[0]
        output_dict["release_year"] = row[1]
        output_list.append(output_dict)
        output_dict = {}
    return output_list


def movie_by_rating(rating_web):
    if rating_web == 'children':
        rating = ('G', 'G')
    elif rating_web == 'family':
        rating = ('G', 'PG', 'PG-13')
    elif rating_web == 'adult':
        rating = ('R', 'NC-17')
    else:
        return 'Не верный рейтинг'
    query = f"SELECT title, rating " \
            f"FROM netflix " \
            f"WHERE rating IN {rating}"
    result_data = select_execute(query)
    output_list = []
    output_dict = {}
    for row in result_data:
        output_dict["title"] = row[0]
        output_dict["rating"] = row[1]
        output_list.append(output_dict)
        output_dict = {}
    return output_list


def movie_by_genre(genre):
    query = f"SELECT show_id, title, listed_in, description " \
            f"FROM netflix " \
            f"WHERE listed_in LIKE '%{genre}%'"
    result_data = select_execute(query)
    output_list = []
    output_dict = {}
    for row in result_data:
        output_dict["show_id"] = row[0]
        output_dict["title"] = row[1]
        output_dict["listed_in"] = row[2]
        output_dict["discription"] = row[3]
        output_list.append(output_dict)
        output_dict = {}
    return output_list


def output_web(content):
    output_str = ''
    for item in content:
        output_str += f'{item} <br>'
    return output_str


def cast_repeated(cast_list, actors):
    cast_else_list = []
    item_cast_list = []
    for item in cast_list:
        str_ = str(item)[2:-3]
        item_cast_list = str_.split(', ')
        for item_cast in item_cast_list:
            if item_cast not in actors:
                cast_else_list.append(item_cast)
    cast_last = []
    for actor in cast_else_list:
        if cast_else_list.count(actor) > 2 and actor not in cast_last:
            cast_last.append(actor)
    return cast_last


def cast_list(*actors):
    query = f"SELECT netflix.cast " \
            f"FROM netflix " \
            f"WHERE netflix.cast LIKE '%{actors[0]}%' or '%{actors[1]}%'"
    result_data = select_execute(query)
    joined_cast = cast_repeated(result_data, actors)
    return joined_cast

# content = cast_list('Jack Black', 'Dustin Hoffman')
# for item in content:
#     print(item)
