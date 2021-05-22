from flask import Flask, request, render_template,jsonify
from werkzeug.exceptions import RequestEntityTooLarge
import publisher
import pymongo
import json
import sys
import bcrypt
import os


#Flask Part
app = Flask(__name__)
data = {"key":"this is default"}
host_ip = sys.argv[1]
db_add = "mongodb://"+host_ip+":27017/"
test_message={}

#database part
myclient = pymongo.MongoClient(db_add)
mydb = myclient["mydatabase"]
mycol = mydb = mydb["key"]

@app.route('/',methods=['GET'])
def entry_point():
    error_msg=""
    return render_template('index.html', error_msg=error_msg)

@app.route('/insert',methods=['POST'])
def insert_db():
    #data = request.get_json() #this part is fect the value from the body
    
    if request.form['psw'] != request.form['psw-repeat']:
        error_msg="Password did not Match"
        return render_template('index.html', error_msg=error_msg)
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        email = request.form['email']
        psw = request.form['psw']
        message = {
            "fname": fname,
            "lname": lname,
            "uname": uname,
            "email": email,
            "psw": bcrypt.hashpw(psw.encode(), bcrypt.gensalt()).decode('utf-8'),
        }
        global test_message
        test_message = message
        result = publisher.publisher(json.dumps(message),host_ip)
        error_msg="New Record Added!"
        return render_template('index.html', error_msg=error_msg)

@app.route('/test',methods=['GET'])
def check():
    if request.args.get('psw') is None:
        global test_message
        return test_message
    else:
        new_psw = request.args.get('psw')
        check = bcrypt.checkpw(new_psw.encode(), test_message['psw'].encode('utf-8'))
        return str(check)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    

