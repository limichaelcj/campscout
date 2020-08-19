import os
import requests
from flask import Flask, request, render_template
app = Flask(__name__)
app.config.from_pyfile('../settings.py')

api_root = 'https://ridb.recreation.gov/api/v1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facilities')
def facilities():

    query = request.args.get('query')

    api_endpoint = f'{api_root}/facilities?query={query}&limit=50&offset=0&state=CA&activity=CAMPING&lastupdated=10-01-2018'
    headers = {
        'accept': 'application/json',
        'apiKey': os.getenv('RIDB_API_KEY')
    }

    response = requests.get(api_endpoint, headers=headers)
    json = response.json()
    facilities = json['RECDATA']

    # request facilities data from ridb
    return render_template('facilities.html', facilities=facilities)
