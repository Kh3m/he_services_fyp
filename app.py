import phe as paillier
from flask import Flask
from flask_restful import Resource, Api

# import resources
from resource.mlm.classification import MyClassification
from resource.enc_dec.enc_dec import EncDec

app = Flask( __name__ )

api = Api(app)

api.add_resource(MyClassification, '/api/operations/ml/classification')
api.add_resource(EncDec, '/api/phe/client/<string:name>')

app.run()
