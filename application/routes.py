from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/bankclassify", methods=['GET', 'POST'])
def bankclassify():

    #extract form inputs
    age = request.form.get("age")
    job = request.form.get("job")
    marital = request.form.get("marital")
    education = request.form.get("education")
    default = request.form.get("default")
    balance = request.form.get("balance")
    housing = request.form.get("housing")
    loan = request.form.get("loan")

   #convert data to json
    input_data = json.dumps({"age": age, "job": job, "marital": marital, "education": education, "default": default, "balance": balance, "housing": housing, "loan": loan})

    #url for bank marketing model
    url = "http://localhost:5000/api"
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", age = age, job = job, marital = marital, education = education, default = default, balance = balance, housing = housing, loan = loan,  results=results.content.decode('UTF-8'))
  
