import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('classifier.pkl', 'rb'))

b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

a = ['Apple', 'Banana', 'blackgram', 'chickpea', 'coconut', 'coffee', 'cotton', 'grapes', 'jute', 'kidney beans', 'lentil', 'maize', 'mango', 'moth beans', 'mung bean', 'muskmelon', 'orange', 'papaya', 'pigeonpeas', 'pomegranate', 'Rice', 'Watermelon']

#buat dataframe label dan angkanya, kayak di notebook


a = pd.DataFrame(a, columns=['label'])
b = pd.DataFrame(b, columns=['encoded'])
classes = pd.concat([a,b], axis=1).set_index('label')

@app.route('/')
def welcome():
    return render_template('crop.html')

@app.route('/', methods=['POST'])
def predict():
    n = request.form.get('n')
    p = request.form.get('p')
    k = request.form.get('k')
    temp = request.form.get('Temperature')
    humid = request.form.get('Humidity')
    pH = request.form.get('PH')
    rain = request.form.get('rain_fall')
    data = [[n,p,k,temp,humid,pH,rain]]
    pred = model.predict(data)

    for i in range(0, len(classes)):
        if(classes.encoded[i]==pred):
            output=classes.index[i].upper()
    return render_template('crop.html', prediction_text=format(output))

if __name__ == "__main__":
    app.run(debug=True)
