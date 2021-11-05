from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

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

@app.route("/ninjas",methods=["POST"])
def new_ninja():
    data = {
        
    }