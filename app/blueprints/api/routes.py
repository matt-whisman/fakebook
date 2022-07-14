from flask import jsonify, render_template, request, redirect
from app.blueprints.main.models import Post
from . import bp as app
from app import db


@app.route('/users')
def users():
    user_dict = {
        "lucas": {
            "eyeColor": "blue",
            "hairColor": "brown"
        },
        "joe": {
            "eyeColor": "gray",
            "hairColor": "black"
        },
        "kevin": {
            "eyeColor": "green",
            "hairColor": "blonde"
        }
    }
    return jsonify(user_dict)


@app.route('/status-update', methods=["POST"])
def status_update():
    status_input = request.form['statusInput']
    user = 1
    
    new_post = Post(body=status_input, user_id=user)
    db.session.add(new_post)
    db.session.commit()
    print(Post.query.all())
    return redirect("localhost:5000")
