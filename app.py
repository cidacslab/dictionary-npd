from flask import Flask, request, render_template
import os
import json
import pandas as pd
from pymongo import MongoClient

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates/')

app = Flask(__name__, template_folder=template_path)
app.config['MONGO_DBNAME'] = 'dictionaryDB'
app.config["MONGO_URI"] = "mongodb://localhost:27017/dictionaryDB"

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/teste', methods=['POST']) 
def teste():
        nameDictionary = str(request.form.get('nameDictionary'))
        variables = str(request.form.get('result'))
    
        variables  = variables.replace("'",'"').replace('-,','-').split('-')

        for var in variables:
                if var is not '':
                        try:
                                var = var.replace(",}","}")
                                var = json.loads(var)
                        except:
                                return "erro"
                        mongo.db[nameDictionary].insert(var)    
        return str(variables),nameDictionary
        
def pandas_to_csv():
        client = MongoClient('localhost', 27017)
        db = client.dictionaryDB
        collection = db.hans

        df = pd.DataFrame(list(collection.find()))
        df[['variable','categories_std','type'].to_csv('/dictionary/name.csv',index=False)