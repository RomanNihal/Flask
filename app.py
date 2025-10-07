from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Started flask"

@app.route('/test')
def test():
    response = make_response("this is a test")
    response.status_code = 202
    response.headers["content-type"] = "text/plain" 
    return response

@app.route('/name/<name>')
def variable(name):
    return f"hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def handle_params():
    if "name" in request.args.keys() and "age" in request.args.keys():
        name = request.args['name']
        age = request.args.get("age")
        return f"{name} is {age} years old"
    else:
        return "missing parameters"
    
@app.route('/getpost', methods=['GET', 'POST'])
def getpost():
    if request.method == "GET":
        return "this is a get request"
    elif request.method == "POST":
        return "this is a post request"
    else:
        return "whatever"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)