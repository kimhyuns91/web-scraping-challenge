from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of our Flask app.
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
info = mongo.db.info

@app.route("/")
def index():
    mars_data = info.find_one()
    return render_template("index.html", mars=mars_data)
    # return("hi")


@app.route("/scrape")
def scrape():  

    mars_data= scrape_mars.scrape()
    mars_data=info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

