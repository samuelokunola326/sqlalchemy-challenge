#importing dependencies
import pandas as pd
import sqlalchemy

# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# import Flask
from flask import Flask, jsonify
######################################################################
# Database setup
######################################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#######################################################################
# Flask setup
# ##################################################################### 

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return ("These are the routes availible<br>"
    
    "Home(Current)<br>"
    "/api/v1.0/precipitation_Normal - Review Percipitation for the Year<br>"
    "/api/v1.0/precipitation_jsonified - Review Percipitation(json form) for the Year<br>"
    "/api/v1.0/stations - See Current stations<br>"
    "/api/v1.0/tobs - Review Temp for the Year<br>"
    "/api/v1.0/tobs_jsonified - Review Temp(json form) for the Year<br>"
    "/api/v1.0/start/<start> - Review Temp for a given date  and forward based on your input <br>"
    "/api/v1.0/start/<start>/end/<end> - Review Temp for a given date range based on your input<br>"
    
    )




# Percipitaion route
@app.route("/api/v1.0/precipitation_Normal")
def prcp():

    # creating connection to sqllite engine
    conn = engine.connect()

    print("Server received request for 'Percipitation' page...")
    # reading data into a data frame
    prcp_df = pd.read_sql('SELECT date, prcp FROM measurement WHERE date BETWEEN "2016-08-23" AND "2017-08-23"',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    prcp_dict = prcp_df.set_index('date').T.to_dict('list')

    #Returning data on web page
    return prcp_dict


# Percipitaion route(jsonify)
@app.route("/api/v1.0/precipitation_jsonified")
def prcp_json():

     # creating connection to sqllite engine
    conn = engine.connect()

    print("Server received request for 'Percipitation' page...")
    # reading data into a data frame
    prcp_df = pd.read_sql('SELECT date, prcp FROM measurement WHERE date BETWEEN "2016-08-23" AND "2017-08-23"',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    prcp_dict = prcp_df.set_index('date').T.to_dict('list')

    #Returning data on web page
    print("Server received request for 'Percipitation_json' page...")
    return jsonify(prcp_dict)



# station route
@app.route("/api/v1.0/stations")
def station():

    # creating connection to sqllite engine
    conn = engine.connect()

    print("Server received request for 'Percipitation' page...")
    # reading data into a data frame
    sts_df = pd.read_sql('SELECT station, name FROM station',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    sts_dict = sts_df.set_index('station').T.to_dict('list')

    #Returning data on web page
    print("Server received request for 'station_json' page...")
    return jsonify(sts_dict)
    



# Temperature route
@app.route("/api/v1.0/tobs")
def tobs():

    # creating connection to sqllite engine
    conn = engine.connect()

    print("Server received request for Tempurature page...")
    # reading data into a data frame
    prcp_df = pd.read_sql('SELECT date, tobs FROM measurement WHERE date BETWEEN "2016-08-23" AND "2017-08-23"',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    tobs_dict = prcp_df.set_index('date').T.to_dict('list')

    #Returning data on web page
    print("Server received request for Tempurature page...")
    return tobs_dict


#  Temperature(json) route
@app.route("/api/v1.0/tobs_jsonified")
def station_json():

    # creating connection to engine
    conn = engine.connect()

    print("Server received request for Tempurature page...")
    # reading data into a data frame
    prcp_df = pd.read_sql('SELECT date, tobs FROM measurement WHERE date BETWEEN "2016-08-23" AND "2017-08-23"',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    tobs_dict = prcp_df.set_index('date').T.to_dict('list')

    #Returning data on web page
    print("Server received request for Tempurature page...")
    return jsonify(tobs_dict)
    
    

# Tempurature based on start date (user input)
@app.route("/api/v1.0/start/<start>")
def start_date(start):

    # creating connection to engine
    conn = engine.connect()

    print("Server received request for Tempurature page...")
    # reading data into a data frame
    tobs_df = pd.read_sql(f'SELECT date, AVG(tobs), MIN(tobs), MAX(tobs) FROM measurement GROUP BY date HAVING date >= {start}',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    tobs_st_dict = tobs_df.set_index('date').T.to_dict('list')

    #Returning data on web page
    print("Server received request for Tempurature page...")


    return jsonify(tobs_st_dict)

    # Tempurature based on date range (user input)
@app.route("/api/v1.0/start/<start>/end/<end>")
def start_end_date(start, end):

    # creating connection to engine
    conn = engine.connect()

    print("Server received request for Tempurature page...")
    # reading data into a data frame
    tobs_se_df = pd.read_sql(f'SELECT date, AVG(tobs), MIN(tobs), MAX(tobs) FROM measurement GROUP BY date HAVING date BETWEEN "{start}" AND "{end}"',conn)

    #closing connection
    conn.close()

    # creating dictionary by setting date to index and then transposing into a dictionary
    tobs_se_dict = tobs_se_df.set_index('date').T.to_dict('list')

    #Returning data on web page
    print("Server received request for Tempurature page...")

    return jsonify(tobs_se_dict)


if __name__ == "__main__":
    app.run(debug=True)