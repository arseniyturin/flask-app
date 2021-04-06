from flask import Flask, request, jsonify
from flask import render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('data.csv')
    stroke = df.stroke.value_counts()
    bmi = df[df.bmi.notna()].bmi.tolist()
    age = df[df.bmi.notna()].age.tolist()
    return render_template('index.html', active_page='index', data={'bmi': bmi, 'age': age})

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
