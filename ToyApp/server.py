from flask import Flask
from flask_restful import Api
import pandas as pd

from users import Users
from locations import Locations

app = Flask(__name__)
api = Api(app)
                    
api.add_resource(Users, '/users')  # add endpoints
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()  # run our Flask app