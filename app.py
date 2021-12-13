# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:16:18 2021

@author: IIOT27
"""

"""import flask
import pickle
# Use pickle to load in the pre-trained model
with open(f'model/heart_disease.pkl','rb') as f:model = pickle.load(f)
app = flask.Flask(__name__,template_folder='template')
@app.route('/')
def main():
    return (flask.render_template('main.html'))
if( __name__ == '__main__'):
    app.run()"""
    
    # -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('heart_disease.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('main.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('main.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('main.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()