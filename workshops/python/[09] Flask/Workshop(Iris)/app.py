import os

import numpy as np 
import pickle
from flask import Flask, render_template, request

classes = ['Setosa', 'Versicolor', 'Virginica']
iris_model = pickle.load(open('res/iris_model.pkl', 'rb'))

app = Flask(__name__)

def predictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,4)
    return iris_model.predict(to_predict)[0]

@app.route('/')
def index():
    return render_template('index.html', title="Iris Species Classification")

@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.form.to_dict()
    to_predict_list = list(to_predict_list.values())
    to_predict_list = list(map(float, to_predict_list))
    flower = classes[predictor(to_predict_list)]
    
    return render_template('predict.html', prediction=flower)

if __name__ == "__main__":
    app.run(debug=True)