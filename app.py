import numpy as np
from flask import Flask, render_template, request, url_for
import pickle

#Inisialisasi flask app
app = Flask(__name__)

#Memuat model
model = pickle.load(open("modellrganda", "rb"))

@app.route('/', methods=['GET','POST'])
def alatprediksi():
    if request.method=='POST':
        if request.form:
            h_open = request.form['open']
            h_low  = request.form['low']
            h_close= request.form['close']

            prediksi = model.predict([[h_open, h_low, h_close]])
            txt_index = 'index.html'
            return render_template('alatprediksi.html', prediction_text='$USD %2f'%prediksi +'/ETH')
    return render_template('index.html')

@app.route('/tentangkami')
def totentangkami():
    return render_template('tentangkami.html')

@app.route('/templates')
def toindex():
    return render_template('index.html')

@app.route('/alatprediksi')
def toalatprediksi():
    return render_template('alatprediksi.html')

@app.route('/tentangkami')
def idx_tentangkami():
    return render_template('tentangkami.html')

@app.route('/templates')
def ttgKami_index():
    return render_template('index.html')

@app.route('/alatprediksi')
def ttgKami_alatprediksi():
    return render_template('alatprediksi.html')


    
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/')
# def tentangkami():
#     return render_template('tentangkami.html')

if __name__ == '__main__':
    app.run(debug=True)