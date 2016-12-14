from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import utils.master
import utils.ticketmaster
import utils.ticketleap
import utils.seatgeek

app = Flask(__name__)

app.secret_key = 'key goes here'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=["POST"])
def output():
    eventList = []
    if "searchTerm" in request.form:
        if request.form["searchTerm"] == "":
            eventList = [['No events found. Please try again.','','','#','','','','']]
        else:
            eventList = utils.master.byPriceAsc(request.form["searchTerm"],int(request.form["minPrice"]),int(request.form["maxPrice"]))
            if not eventList:
                eventList = [['No events found. Please try again.','','','#','','','','']]
            session['searchTerm'] = request.form['searchTerm']
            session['minPrice'] = request.form['minPrice']
            session['maxPrice'] = request.form['maxPrice']
    else:
        if request.form["filterbuttons"] == "filterPA":
            eventList = utils.master.byPriceAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterPD":
            eventList = utils.master.byPriceDes(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterDA":
            eventList = utils.master.byDateAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterDD":
            eventList = utils.master.byDateDes(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterAA":
            eventList = utils.master.byPriceAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterAD":
            eventList = utils.master.byPriceAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
    
    return render_template("output.html",events=eventList)

@app.route("/login", methods=["POST"])
def login():
    return None

if __name__ == "__main__":
    app.debug = True
    app.run()
 
