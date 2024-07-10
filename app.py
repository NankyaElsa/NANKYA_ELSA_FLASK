
from flask import Flask, render_template, request, redirect, url_for

#create an instance of a flask class
app = Flask(__name__)

#create wildConservation species List
species_list = [
    {"name": "Elephant", "habitat": "Africa"},
    {"name": "Lion", "habitat": "Africa"},
    {"name": "Giraffe", "habitat": "Africa"},
    {"name": "Tiger", "habitat": "Africa"},
    {"name": "Bat", "habitat": "Africa"},
    {"name": "Penguin", "habitat": "Antarctica"},
    {"name": "Seal", "habitat": "Antarctica"},
    {"name": "Eagle", "habitat": "Antarctica"},
    {"name": "Falcon", "habitat": "Antarctica"},
    {"name": "Ostrich", "habitat": "Antarctica"}
]

@app.route('/')
def index():
    return render_template("index.html", species_list=species_list)

@app.route('/add', methods=['GET', 'POST'] )
def add_species():
    if request.method == 'POST':
        name = request.form["name"]
        habitat = request.form["habitat"]
        species_list.append({"name": name, "habitat": habitat})
        return redirect(url_for("index"))
    return render_template("add_species.html")