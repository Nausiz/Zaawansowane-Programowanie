from Services.Utils import read_file
from Models.Link import Link
from Models.Movie import Movie
from Models.Rating import Rating
from Models.Tag import Tag
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self) -> str:
        return f"Modele: /links, /movies, /ratings, /tags"


class LinksData(Resource):
    def get(self) -> list:
        return get_links_data()


class MoviesData(Resource):
    def get(self) -> list:
        return get_movies_data()


class RatingsData(Resource):
    def get(self) -> list:
        return get_ratings_data()


class TagsData(Resource):
    def get(self) -> list:
        return get_tags_data()


def get_links_data() -> list:
    links_data = read_file("Data/links.csv")
    links_data_list = []
    for row in links_data:
        links_data_list.append(Link(row[0], row[1], row[2]).__dict__)
    return links_data_list


def get_movies_data() -> list:
    movies_data = read_file("Data/movies.csv")
    movies_data_list = []
    for row in movies_data:
        movies_data_list.append(Movie(row[0], row[1], row[2]).__dict__)
    return movies_data_list


def get_ratings_data() -> list:
    ratings_data = read_file("Data/ratings.csv")
    ratings_data_list = []
    for row in ratings_data:
        ratings_data_list.append(Rating(row[0], row[1], row[2], row[3]).__dict__)
    return ratings_data_list


def get_tags_data() -> list:
    tags_data = read_file("Data/tags.csv")
    tags_data_list = []
    for row in tags_data:
        tags_data_list.append(Tag(row[0], row[1], row[2], row[3]).__dict__)
    return tags_data_list
