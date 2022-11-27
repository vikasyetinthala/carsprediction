from flask import Flask,render_template,redirect,url_for,request
import pickle
from sklearn.metrics import *
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

app=Flask(__name__)

model=pickle.load(open('carsmodel1.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict():
    year=eval(request.form['year'])
    year=2020-(year)
    presentprice=eval(request.form['presentprice'])
    km_driven=eval(request.form['km_driven'])
    fuel=request.form['fuel']
    if fuel.lower()=='petrol':
        fuel_type_petrol=1
        fuel_type_diesel=0
    elif fuel.lower()=='diesel':
        fuel_type_diesel=1
        fuel_type_petrol=0
    else:
        fuel_type_diesel=0
        fuel_type_petrol=0
    seller=request.form['seller']
    if seller.lower()=='individual':
        seller_type=1
    else:
        seller_type=0
    trans=request.form['transmission']
    if trans.lower()=='manual':
        transmission_manual=1
    else:
        transmission_manual=0
    owner=eval(request.form['owner'])
    output=model.predict([[year,presentprice,km_driven,fuel_type_petrol,fuel_type_diesel,seller_type,transmission_manual,owner]])
    return render_template('index.html',output=output)




if __name__=='__main__':
    app.run()
