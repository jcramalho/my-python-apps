from flask_restful import Resource, reqparse

class Processos(Resource):
    def get(self):
        return {'data': data}, 200  # return data and 200 OK

    