from Services.Repository import HelloWorld, LinksData, MoviesData, RatingsData, TagsData
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(LinksData, '/links')
api.add_resource(MoviesData, '/movies')
api.add_resource(RatingsData, '/ratings')
api.add_resource(TagsData, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
