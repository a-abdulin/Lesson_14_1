from project.utils import movie_by_title, movie_by_year, movie_by_rating, movie_by_genre, output_web
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_start():
    return "Начальная страница"


@app.route("/movie/<movie_title>")
def page_movie(movie_title):
    content = movie_by_title(movie_title)
    return f'Title: {content["title"]} <br>' \
           f'Country: {content["country"]} <br>' \
           f'Release_year: {content["release_year"]} <br>' \
           f'Description: {content["description"]}'


@app.route("/movie/<year1>/to/<year2>/")
def page_movie_by_year(year1, year2):
    content = movie_by_year(year1, year2)
    return output_web(content)


@app.route("/rating/<rating>")
def page_movie_by_rating(rating):
    content = movie_by_rating(rating)
    return output_web(content)


@app.route("/genre/<genre>")
def page_movie_by_genre(genre):
    content = movie_by_genre(genre)
    return output_web(content)


app.run()
