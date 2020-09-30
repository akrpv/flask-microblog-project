from app import app
from flask import render_template


@app.route('/')
def index():
    names = ['Ivan']
    return render_template('index.html', n=names)
