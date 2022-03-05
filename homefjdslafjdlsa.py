# Jarandon Adams 1812590
# CIS 3368 O.Dobretsberger
# Homework 2

import flask
from flask import jsonify
from flask import request, make_response
import mysql.connector
from mysql.connector import Error
from sql import create_connection
import hashlib

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print("Success! A connection has been established")
    except Error as e:
        print(f"ERROR! The error '{e}' has occured")
    return connection

conn = create_connection("cis3368sp22.cscqb2tpprgr.us-east-2.rds.amazonaws.com", "admin22", "Bearkat3500!", "CIS3368SP22_DB")  # will establish a secure connection to the database
cursor = conn.cursor(dictionary=True)   # format as dictionary
sql = "Select * FROM zoo, logs"   # will select the table celestialobjects from the connected database
cursor.execute(sql)
rows = cursor.fetchall()   

def execute_query(connection, query):  # establishing the execute_query statement
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("SUCCESS! The Query has Been Executed Successfully")   # success indicatior
    except Error as e:
        print(f"ERROR! The error '{e} has occurred")    # Error message

def execute_read_query(connection, query):    # # establishing the execute_read_query statement
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"ERROR! The error '{e}' has occurred")   # Error message



# will set up an application name
app = flask.Flask(__name__) # will set up the application
app.config["DEBUG"] = True # will allow errors to be shown in the browser

# will print the entire zoo table with all the animal records within
@app.route('/api/animals', methods=['GET'])
def animals():
    conn = create_connection("cis3368sp22.cscqb2tpprgr.us-east-2.rds.amazonaws.com", "admin22", "Bearkat3500!", "CIS3368SP22_DB")
    sql = "SELECT * FROM zoo"    # selects all data from the zoo table
    guestlist = execute_read_query(conn,sql)
    results = []
    for animals in zoo:
        results.append animals)
    return jsonify(results)    #which data will be returned


# will add a new animal into the zoo table and log the event to the logs table
@app.route('/api/addanimal', methods=['POST'])
def new_animal():
    request_data = request.get_json()
    newanimal = request_data['animal']
    newgender = request_data['gender']        # this area contains the information that will be added to the db table
    newsubtype = request_data['subtype']
    newage = request_data['age']
    newcolor = request_data['color']


    conn = create_connection("cis3368sp22.cscqb2tpprgr.us-east-2.rds.amazonaws.com", "admin22", "Bearkat3500!", "CIS3368SP22_DB")    # database connection
    sql1 = "INSERT INTO zoo (animal, gender, subtype, age, color) VALUES ('%s', '%s', '%s', '%s', '%s')" % (newanimal, newgender, newsubtype, newage, newcolor)   # variables to be inputted into the table
    execute_query(conn, sql)
    
    request_data = request.get_json()
    logdate = request_data['date']   # YYYY-MM-DD format for the date
    loganimalid = request_data['name']   # name of mechanic
    comment = "The new animal " + str(new_animal) + " has been added"

    sql2 = "INSERT INTO log (name, message, date) VALUES (%s, %s, '%s')" % (logdate, logname, logmessage)    # insert inputted data into logs table
    execute_query(conn, sql2)
    return 'SWEET, THE CAR WAS SUCCESSFULLY ADDED AND LOGGED.'  # message that will show in the body if the post method is executed correctly


# will delete a car from the car table based on the id provided
@app.route('/api/deleteanimal', methods=['DELETE'])   # creating a access token which will be required in order to execute the delete method
def del_animal():
    request_data = request.get_json()
    delete_car_id = request_data['id']   # id being requested

    conn = create_connection("cis3368.cn0r90kgsnij.us-east-2.rds.amazonaws.com", "admin1", "Jarandon35002000", "CIS3368FA21")   # database connection
    sql = "DELETE FROM cars WHERE id = = %s" % (delete_car_id)    # will delete the item selected above completely based on its unique ID which is auto incremented
    execute_query(conn, sql)

    request_data = request.get_json()
    logdate = request_data['date']   # YYYY-MM-DD format for the date
    logname = request_data['name']   # name of mechanic
    logmessage = request_data['message']   # short log message

    sql2 = "INSERT INTO log (name, message, date) VALUES (%s, %s, '%s')" % (logdate, logname, logmessage)    # insert inputted data into logs table
    execute_query(conn, sql2)
    return 'SEEYA LATER, THE CAR WAS SUCCESSFULLY DELETED AND LOGGED'   # message that will show in the body if the post method is executed correctly


# will add a new mechanic into the mechanic table
@app.route('/api/addmechanic', methods=['POST'])
def add_mechanic():
    request_data = request.get_json()
    newfirstname = request_data['firstname']
    newlastname = request_data['lastname']        # this area contains the information that will be added to the db table
    newtitle = request_data['title']
    newcurrentcar = request_data['currentcar']


    conn = create_connection("cis3368.cn0r90kgsnij.us-east-2.rds.amazonaws.com", "admin1", "Jarandon35002000", "CIS3368FA21")  # database Connection
    sql = "INSERT INTO mechanic (firstname, lastname, title, currentcar) VALUES (%s, %s, %s, %s)" % (newfirstname, newlastname, newtitle, newcurrentcar)   # variables to be inserted 
    execute_query(conn, sql)

    request_data = request.get_json()
    logdate = request_data['date']   # YYYY-MM-DD format for the date
    logname = request_data['name']   # name of mechanic
    logmessage = request_data['message']   # short log message

    sql2 = "INSERT INTO log (name, message, date) VALUES (%s, %s, '%s')" % (logdate, logname, logmessage)    # insert inputted data into logs table
    execute_query(conn, sql2)
    return 'SWEET, THE MECHANIC WAS SUCCESSFULLY ADDED AND LOGGED'  # message that will show in the body if the post method is executed correctly


# will delete a car from the cars table based on the id provided
@app.route('/api/deletemechanic', methods=['DELETE'])   # creating a access token which will be required in order to execute the delete method
def del_mechanic():
    request_data = request.get_json()
    delete_car_id = request_data['id']

    conn = create_connection("cis3368.cn0r90kgsnij.us-east-2.rds.amazonaws.com", "admin1", "Jarandon35002000", "CIS3368FA21")
    sql = "DELETE FROM cars WHERE id = = %s" % (delete_car_id)    # will delete the item selected above completely based on its unique ID which is auto incremented
    execute_query(conn, sql)

    request_data = request.get_json()
    logdate = request_data['date']   # YYYY-MM-DD format for the date
    logname = request_data['name']   # name of mechanic
    logmessage = request_data['message']   # short log message

    sql2 = "INSERT INTO log (name, message, date) VALUES (%s, %s, '%s')" % (logdate, logname, logmessage)    # insert inputted data into logs table
    execute_query(conn, sql2)
    return 'SO LONG, THE MECHANIC WAS SUCCESSFULLY DELETED AND LOGGED'   # message that will show in the body if the post method is executed correctly


# will assign a car to a specific mechanic
@app.route('/api/assigncar', methods=['POST'])
def auth_assign():
    if request.authorization:
        encoded=request.authorization.password.encode() #unicode encoding
        hashedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == 'admin'and hashedResult.hexdigest() == password:    # username and password are authenticated
            return '<h1> SUCCESS </h1>'   # success message
    return make_response('ERROR, COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})    # Error message

def assign_car():
    request_data = request.get_json()
    mechanic_id = request_data['id']   # mechanic id from mechanic table
    car_id = request_data['id']    #car id from car table


    conn = create_connection("cis3368.cn0r90kgsnij.us-east-2.rds.amazonaws.com", "admin1", "Jarandon35002000", "CIS3368FA21")  # database connection
    sql = "INSERT INTO mechanic (currentcar) SELECT mechanic.id, car.id FROM mechanic, car WHERE id = = %s %s" % (mechanic_id, car_id)   # assigns a car to a mechanic by id
    execute_query(conn, sql)
    return 'NICE, THE MECHANIC WAS SUCCESSFULLY ASSIGNED TO THE VEHICLE'  # message that will show in the body if the post method is executed correctly



# will unassign a car from a specific mechanic
@app.route('/api/unassigncar', methods=['POST'])
def auth_unassign():
    if request.authorization:
        encoded=request.authorization.password.encode() #unicode encoding
        hashedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == username and hashedResult.hexdigest() == password:
            return '<h1> SUCCESS </h1>'
    return make_response('ERROR, COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

def unassign_car():
    request_data = request.get_json()
    mechanic_id = request_data['id']  # mechanic id from mechanic table
    car_id = request_data['id']   # car id from car table


    conn = create_connection("cis3368.cn0r90kgsnij.us-east-2.rds.amazonaws.com", "admin1", "Jarandon35002000", "CIS3368FA21")   # database connection
    sql = "DELETE FROM currentcar.mechanic SELECT mechanic.id, car.id FROM mechanic, car WHERE id = = %s %s" % (mechanic_id, car_id)   # unassigns a car from the mechanic using id
    execute_query(conn, sql)
    return 'ADIOS, THE MECHANIC WAS SUCCESSFULLY UNASSIGNED FROM THE VEHICLE'  # message that will show in the body if the post method is executed correctly



# will return all logs from within the logs table
@app.route('/api/logs', methods=['GET'])
def get_logs():
    conn = create_connection("cis3368sp22.cscqb2tpprgr.us-east-2.rds.amazonaws.com", "admin22", "Bearkat3500!", "CIS3368SP22_DB")   # database connection
    sql = "SELECT * FROM logs ORDER BY date DESC"    # selects all data from the logs table and orders it by date in descending order (most recent logs first)
    logs = execute_read_query(conn,sql)
    results = []
    for details in logs:
        results.append(details)
    return jsonify(results)    # all recorded logs data will be returned



app.run()
