from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route("/")
def to_users():

    return redirect("/users")

@app.route("/users")
def users():

    users = User.get_all()

    return render_template("users.html", all_users = users)

@app.route("/users/new")
def new_user():

    return render_template("new_user.html")

@app.route("/users/add", methods=["POST"])
def add_user():

    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.create(data)

    return redirect("/users")

@app.route("/users/<int:user_id>")
def get_one_by_id(user_id):
    data_dictionary = {
        "id": user_id
    }
    one_user = User.get_one_by_id(data_dictionary)

    return render_template("user_profile.html", one_user=one_user[0])

@app.route("/users/<int:user_id>/edit")
def edit(user_id):
    data_dictionary = {
        "id": user_id
    }
    one_user = User.get_one_by_id(data_dictionary)
    return render_template("edit_user.html", one_user=one_user[0])

@app.route("/users/<int:user_id>/update", methods=["POST"])
def update(user_id):
    data_dictionary = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "id":user_id
    }
    User.edit(data_dictionary)
    return redirect(f"/users/{user_id}")

@app.route("/users/<int:user_id>/destroy")
def destroy(user_id):
    data_dictionary={
        "id":user_id
    }
    User.destroy(data_dictionary)
    return redirect("/users")