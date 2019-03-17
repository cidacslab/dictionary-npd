from flask import Flask, request, render_template
import os
import json

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates/')

app = Flask(__name__, template_folder=template_path)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/teste', methods=['POST']) 
def teste():
    values = str(request.form.get('result'))
    print (values.replace('-,','-'))
    print (values.replace('-,','-').split('-'))
    return values

