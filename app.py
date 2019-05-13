from flask import Flask, request, render_template
import os
import sys
import json
import pandas as pd
import re
from pymongo import MongoClient
from bson.objectid import ObjectId

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates/')

app = Flask(__name__, template_folder=template_path)
# app.config['MONGO_DBNAME'] = 'dictionaryDB'
# app.config["MONGO_URI"] = "mongodb://localhost:27017/dictionaryDB"

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
#ObjectId = require('mongodb').ObjectID

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/dictionary')
def dictionary():
        dic = db.collection_names(include_system_collections=False) #Incluir select para buscar todos os dicionarios no banco.
        dictionarys = []
        for i in dic:
                dictionarys.append(i)
        return render_template('dictionary.html', dictionarys=dictionarys)

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
                        collection = db[nameDictionary]
                        collection.insert(var) 

        dic_submit = db.collection_names(include_system_collections=False) #Incluir select para buscar todos os dicionarios no banco.
        dics_submit = []
        for i in dic_submit:
                dics_submit.append(i)
           
        return render_template('dictionary.html', dictionarys=dics_submit)

@app.route('/update', methods=['POST'] )
def update():
        nameDic_update = str(request.form.get('nameDictionary'))
        variable_update = str(request.form.get('result'))
        id_update = str(request.form.get('id_var'))

        variable_update  = variable_update.replace("'",'"').replace('-', '').replace(",}","}")
        variable_update = json.loads(variable_update)

        db[nameDic_update].update({'_id': ObjectId(id_update)}, {'$set': variable_update }, upsert = True)
               
        db_update_list = list(db[nameDic_update].find())
        return render_template('variables.html', dict = nameDic_update, variables = db_update_list)


@app.route('/to_csv', methods=['POST'])
def pandas_to_csv():

        nameDictionary_csv = str(request.values.get('id'))
        
        collection = db[nameDictionary_csv]

        df = pd.DataFrame(list(collection.find()))
        
        df = df[['variable','categories_std','type']]
        path_csv = ('/dictionary/'+nameDictionary_csv+'.csv')
        my_file = os.getcwd()
        df.to_csv(my_file+path_csv,index=False)
        return render_template('index.html')

@app.route("/edit_dictionary", methods=['GET', 'POST'])
def edit_dictionary():
        nameDictionary_edit = str(request.values.get('id'))
        db_edit = db[nameDictionary_edit]
        db_edit_list = list(db_edit.find())
        return render_template('variables.html', dict = nameDictionary_edit, variables = db_edit_list) 

@app.route("/search")
def search():
        nameDictionary_search = str(request.args.get('dictionary'))
        analise = re.compile(nameDictionary_search)
        collection = db.collection_names(include_system_collections=False)
        search_dic = []
        for i in collection:
                if analise.search(i):
                        search_dic.append(i)
        #list(db.hans.find())
        return render_template('dictionary.html', dictionarys = search_dic)

@app.route('/dictionary_delete', methods=['GET', 'POST'])
def dictionary_delete():
        nameDictionary_delete = str(request.values.get('id'))
        collection = db[nameDictionary_delete]
        collection.drop()

        dic = db.collection_names(include_system_collections=False) #Incluir select para buscar todos os dicionarios no banco.
        dictionarys = []
        for i in dic:
                dictionarys.append(i)
        return render_template('dictionary.html', dictionarys=dictionarys)

@app.route('/variable_delete', methods=['GET', 'POST'])
def variable_delete():
        name_variable_delete = str(request.values.get('id')).split()
        col_var_del = db[name_variable_delete[0]].remove( { '_id': (ObjectId(name_variable_delete[1])) }, 1)

        db_edit_del = db[name_variable_delete[0]]
        db_edit_list_del = list(db_edit_del.find())
        return render_template('variables.html', dict = name_variable_delete[0], variables = db_edit_list_del)

@app.route('/edit_variable', methods=['GET', 'POST'])
def edit_variable():
        name_variable_edit = str(request.values.get('id')).split()
        col_var_edit =  list(db[name_variable_edit[0]].find({'_id': ObjectId((name_variable_edit[1])) }))
        return render_template('edit.html', dict = name_variable_edit[0], vars = col_var_edit)



        
