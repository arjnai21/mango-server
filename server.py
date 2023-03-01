# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
import json
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# country list (if "" then all)
# geographic boundaries list (long, lat, range)
# carrier list
# operating system list
# device type list
# make string
# model list

map = {
        "country" : [],
        "geographic_boundaries" : [
                {
                "lat": 0,
                "long": 3,
                "range": 5
                },
        ],
        "carrier_list": [],
        "operating_system": [],
        "device_type": [],
        "make" : "",
        "model": [],
        "id": 1,
        "endpoint": "",

        "company_name": "",
        "industry": "",
        "logo": "",
        "description": ""
       }
#ad_type should be parameter

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World!'

@app.route('/ad-gen', methods=["POST"])
def generate_ad_request():
    
    if request.headers.get("Content-Type") != "application/json":
        return "send me some json cuzzo"
    content = request.get_json()

    if not ("country" in content and type(content["country"]) == list):
        return "Missing/Invalid country"
    
    if not ("geographic_boundaries" in content and type(content["geographic_boundaries"]) == list):
        return "Missing/Invalid geographic_boundaries"
    else:
        for i in content["geographic_boundaries"]:
            if not ("lat" in i and "long" in i and "range" in i and len(i) == 3): # check types as well (float)
                return "Missing/Invalid lat/long/range"
        
    if not ("carrier_list" in content and type(content["carrier_list"]) == list):
        return "Missing/Invalid carrier_list"

    if not ("operating_system" in content and type(content["operating_system"]) == list):
        return "Missing/Invalid operating_system"
    
    if not ("device_type" in content and type(content["device_type"]) == list):
        return "Missing/Invalid device_type"
    
    if not ("make" in content and type(content["make"]) == str):
        return "Missing/Invalid make"
    
    if not ("model" in content and type(content["model"]) == list):
        return "Missing/Invalid model"
    
    if not ("id" in content and type(content["id"]) == int):
        return "Missing/Invalid id"
    
    if not ("endpoint" in content and type(content["endpoint"]) == str):
        return "Missing/Invalid endpoint"
    
    if not ("company_name" in content and type(content["company_name"]) == str):
        return "Missing/Invalid company_name"
    
    if not("industry" in content and type(content["industry"]) == str):
        return "Missing/Invalid industry"
    
    if not("logo" in content and type(content["logo"]) == str):
        return "Missing/Invalid logo"
    
    if not("description" in content and type(content["description"]) == str):
        return "Missing/Invalid description"

    f = open("content.json", "w")
    f.write(json.dumps(content))
    f.close()   

    return "Success"
    
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=4949, debug=True)