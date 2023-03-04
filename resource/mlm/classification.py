from flask_restful import Resource, request

class MyClassification(Resource):
    def post(self):
        data = request.get_json()
        return data, 200
    