from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import redirect

from user import User
app = Flask(__name__)
@app.route("/")
def index():
    return redirect("/users")

@app.route('/users')
def select_all():
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route("/users/new")
def create_form():
    return render_template("insert.html")

@app.route("/users/new/insert", methods=['POST'])
def insert():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    user = User.save(data)
    return redirect(f'/users/{user.id}')

@app.route('/users/<int:user_id>')
def slecet_one(user_id):
    data = {
        "id": user_id
    }
    user = User.get_one(data)
    return render_template("selectOne.html", user = user)

@app.route('/users/<int:user_id>/edit_form')
def edit_form(user_id):
    data = {
        "id": user_id
    }
    user = User.get_one(data)
    return render_template("update.html", user = user)

@app.route("/users/<int:user_id>/edit", methods=['POST'])
def update(user_id):
    data = {
        "id" : user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.update(data)
    return redirect(f'/users/{user_id}')

@app.route("/users/<int:user_id>/remove")
def remove(user_id):
    data = {
        "id" : user_id
    }
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)