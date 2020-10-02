from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import Post, Tag
from app import db
from .forms import PostForm

import re


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tag_names = re.sub(r'\s+','',request.form['tag']).split(',')

        try:
            post = Post(title=title, content=content)
            for tag_name in tag_names:
                if not Tag.query.filter(Tag.name == tag_name).first():
                    tag = Tag(name=tag_name)
                else:
                    tag = Tag.query.filter(Tag.name == tag_name).first()
                post.tags.append(tag)
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print('exception', e)

        return redirect( url_for('posts.index') )
    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@posts.route('/')
def index():
    posts = Post.query.all()
    q = request.args.get('q')

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.content.contains(q)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)

@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts
    return render_template('posts/tag_detail.html', posts=posts, tag=tag)

@posts.route('/tags')
def tags():
    tags = Tag.query.all()
    return render_template('posts/tags.html', tags=tags)
