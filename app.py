from flask import Flask, request, render_template, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():
  
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)

    collection.insert_one(form_data)
    #print(form_data)

    return 'Data Submited Successfully'

@app.route('/api')
def name():

    name = request.values.get('name')
    age = request.values.get('age')

    result = {
        'name': name,
        'age': age
    }
  
    return 'api response page'

if __name__ == '__main__':

    app.run(debug=True)