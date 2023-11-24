import os
from flask import Flask, render_template

# Get the directory name of the script's location
base_dir = os.path.dirname(os.path.abspath(__file__))

# Set the template folder to one level up and then into the templates directory
template_dir = os.path.join(base_dir, '..', 'templates')

app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About'
