#-*-coding utf-8-*-

import json

from flask import Flask
from flask_restful import Api, Resource

from utils.crawler import Crawler
from utils.sorteio import Sorteia

app = Flask(__name__)
api = Api(app)   
app.config['JSON_AS_ASCII'] = False

class Resultados(Resource):
    def get(self,tipo):
        result =  Crawler(tipo)        
        response = [ i for i in result]
    
        return response
    

class Sorteio(Resource):
    def get(self,tipo,qt):
        result = Sorteia(tipo,qt)
        response = [i for i in result]
        
         
        
        return response
        
api.add_resource(Resultados,'/resultados/<tipo>')
api.add_resource(Sorteio,'/sorteio/<string:tipo>/<int:qt>')

if __name__ == '__main__':
    app.run(debug=True)
    
