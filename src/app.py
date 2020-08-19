from flask import Flask, render_template
app = Flask(__name__)
app.config.from_pyfile('../settings.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facilities')
def facilities():
    # request facilities data from ridb
    return render_template('facilities.html')
