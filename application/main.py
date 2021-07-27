from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

def loadFile():
    with open('MOCK_DATA.json','rb') as f:
        data = json.load(f)
        return data

@app.route('/')
def index():
    return "<h1>Hello from Connor!</h1><h3>This URL with api at the end will return car makes, models, and colors.</h3><p>Copyright Connor Smith 2021</p>"

class myAPI(Resource):
    def get(self):
        return loadFile()

api.add_resource(myAPI,'/api')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
