from flask import Flask, request, jsonify, render_template
import pymongo
import json
import database
import sys

app = Flask(__name__)
host_ip = sys.argv[1]
db_add = "mongodb://"+host_ip+":27018/"

@app.route('/',methods=['GET'])
def entry_point():
    data_ = database.main(db_add)
    return render_template('index.html', data_= data_)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
