# Dependencies
from flask import Flask, jsonify, render_template, request, redirect
import pymongo
import ExtractMarsData as marsData

app = Flask(__name__)


########################  Initializing Mongo with DB ##################
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient()
db = client.marsDSS
collection = db.marsDataSet

########################  Code to Read from Mongo DB ##################
@app.route("/")
def index():
    marsDataMGO = db.marsDataSet.find_one()
    print("Data Pulled...")
    return render_template("index.html", marsInfo = marsDataMGO)
######################################################################

########################  Code to Write to Mongo DB ##################
@app.route("/scrape")
def scrape():
    db.marsDataSet.update( {}, marsData.ExtractMarsData(), upsert = True)
    print("Data Upserted...")
    return redirect("/", code=302)
######################################################################


########################  Code to Run in Background ##################
if __name__ == "__main__":
    app.run(debug=False, port=5016)
######################################################################
