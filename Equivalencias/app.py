from flask import request, Flask, render_template, redirect
from flask_restful import Api
from flask_pymongo import PyMongo
import datetime

from processos import Processos

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/equivalencias2022"
mongo = PyMongo(app)

api = Api(app)
                    
api.add_resource(Processos, '/processos')  # add endpoints
# api.add_resource(Locations, '/locations')


app.run() 