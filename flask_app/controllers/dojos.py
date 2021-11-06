from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html",dojos=dojos)

@app.route("/create",methods=["POST"])
def add_dojo():
    data = {
        "name":request.form["name"]
    }
    Dojo.create_dojo(data)
    return redirect("/")

@app.route("/dojo/<int:id>")
def dojo_info(id):
    data = {
        "id":id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)
    return render_template("show_dojo.html",dojo_ninjas=dojo_ninjas)

    
@app.route("/new")
def add_ninja():
    dojos_ninjas = Dojo.get_all_dojos()
    return render_template("new_ninja.html",dojos_ninjas=dojos_ninjas)

@app.route("/ninjas",methods=["POST"])
def new_ninja():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    new_id = request.form["dojo_id"]
    return redirect(f"/dojo/{new_id}")
