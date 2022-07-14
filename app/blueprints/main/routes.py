from flask import render_template
from . import bp as app
from app.blueprints.main.models import Post


@app.route("/")
def home():
    posts = Post.query.all()
    posts.sort(key=lambda post: post.date_created, reverse=True)
    
    context = {
        "posts": posts,
    }

    return render_template('index.html', **context)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')
