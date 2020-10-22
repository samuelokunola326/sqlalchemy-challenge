# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return ("These are the routes availible<br>"
    
    "Home(Current)<br>"
    "/api/v1.0/precipitation - Review Percipitation for the Year<br>"
    "/api/v1.0/tobs - Review Temp for the Year<br>"
    "/api/v1.0/<start> and /api/v1.0/<start>/<end> - Review Temp for a given date span<br>")




# Percipitaion route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


# Stations route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


# Temperature route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


# Tmperature - date range route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"



# pending may need
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)