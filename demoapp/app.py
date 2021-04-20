from flask import Flask

from flask import request

from flask import jsonify,make_response

from dicom_parser import Image

from os import path

 

import json

import os

import glob

app = Flask(__name__)

 

@app.route("/")

def home():

    return "Hello from flask > app.py file..."

 

@app.route("/patientname")

def readFile():

    args=request.args

    dcmfiles = [f for f in glob.glob(args['filename']+"/*.dcm")]

    # with open(filepath) as f:

    #     print(f.read())

    full_data = []

    for files in dcmfiles:

    #     image=Image(args['filename'])

    #     name=(image.header.get('PatientName'))

        image=Image(files)

        name=(image.header.get('PatientName'))

        print(name)

        full_data.append({"name":name})

        

    with open('test/data.json', 'w') as outfile:

        json.dump(full_data, outfile)

    return make_response(jsonify(full_data), 200)

 

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=int("5011"), debug=True)
