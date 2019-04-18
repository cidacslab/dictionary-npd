from flask import Flask, request, render_template
import os
import sys
import json
import pandas as pd
from pymongo import MongoClient

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates/')

app = Flask(__name__, template_folder=template_path)
# app.config['MONGO_DBNAME'] = 'dictionaryDB'
# app.config["MONGO_URI"] = "mongodb://localhost:27017/dictionaryDB"
<<<<<<< HEAD
client = MongoClient('mongodb://localhost:27017/')
mongo = client.dictionaryDB
    
#     db.cars.insert_many(cars)
# mongo = PyMongo(app)

=======

# mongo = PyMongo(app)
client = MongoClient('mongodb://localhost:27017/')
db = client.dictionaryDB
def pymongo_python_sys():
        if sys.version_info.major == 2:
                app.config['MONGO_DBNAME'] = 'dictionaryDB'
                app.config["MONGO_URI"] = "mongodb://localhost:27017/dictionaryDB"
                mongo = PyMongo(app)
        else:
                client = MongoClient('mongodb://localhost:27017/')
                mongo = client.dictionaryDB
        return mongo

# mongo = pymongo_python_sys()
>>>>>>> 3dbd5aaf54cf6e671d2c123b5ee4c5a9d180e961
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dictionary')
def dictionary():
        dicttionarys = mongo.collection.find(mongo.name_dictionary).all()
        return render_template('dictionary.html')

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
<<<<<<< HEAD
                        mongo.db[nameDictionary].insert(var)
        return str(variables),nameDictionary
        
# def pandas_to_csv():
#         client = MongoClient('localhost', 27017)
#         db = client.dictionaryDB
#         collection = db['']

#         df = pd.DataFrame(list(collection.find()))
#         df[['variable','categories_std','type'].to_csv('/dictionary/name.csv', index=False)
=======
                        collection = db[nameDictionary]
                        collection.insert(var)    
        return render_template('index.html')
# def pandas_to_csv():
#         client = MongoClient('localhost', 27017)
#         db = client.dictionaryDB
#         collection = db.hans

        df = pd.DataFrame(list(collection.find()))
        df[['variable','categories_std','type'].to_csv('/dictionary/name.csv',index=False)
           

@app.route('/dictionary')
def dictionary():0e72578
        return render_template('dictionary.html')
>>>>>>> 3dbd5aaf54cf6e671d2c123b5ee4c5a9d180e961
