from flask import Flask
from flask_restful import Resource, Api

agile = Flask(__name__)
api = Api(agile)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    agile.run(debug=True)