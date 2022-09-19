import json

from project.utils import select_execute

def list_to_json(content):
    json_list = []
    json_dict = {}
    for item in content:
        json_dict["release_year"] = item[0]
        json_dict["title"] = item[1]
        json_dict["type"] = item[2]
        json_dict["listed_in"] = item[3]
        json_list.append(json_dict)
        json_dict = {}
    return json_list


def movie_by_data(type, release_year, listed_in):
    query = f"SELECT release_year, title, type, listed_in " \
            f"FROM netflix " \
            f"WHERE type LIKE '%{type}%' AND release_year={release_year} AND listed_in LIKE '%{listed_in}%' "
    result_data = select_execute(query)
    json_data = list_to_json(result_data)
    return json_data


content = movie_by_data('Movie', 1982, 'Comedie')
# for item in content:
#     print(item)
print(content)
