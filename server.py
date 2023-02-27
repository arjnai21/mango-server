# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/ad-gen', methods=["POST"])
def generate_ad_request():
    print("got request")
    params = request.args.get('param')
    print("got param")
    if request.headers.get("Content-Type") == "application/json":
        print("request was in json")
    print("about to call get_json")
    content = request.get_json(force=True)
    print(content["param"])
    print("hellooo")
    return content
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=4949, debug=True)