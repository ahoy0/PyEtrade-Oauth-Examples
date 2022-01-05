# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class callback(Resource):
    
    def get(self):
        
        token = request.query_string
        
        with open("insert_file_path_here","w") as f:

            f.write(str(token))

            f.close()
        
        return {"data":"I worked"}
    
api.add_resource(callback, '/callback')

if __name__ == "__main__":
    app.run(host="0.0.0.0")