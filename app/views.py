from app import app
from flask import render_template
from posts.blueprint import posts


app.register_blueprint(posts, url_prefix='/blog')

@app.route('/')
def index():
    names = ['pidor']
    return render_template('index.html', n=names)
