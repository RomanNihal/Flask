from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Started flask"

@app.route('/abc')
def test():
    return "this is a test"

@app.route('/name/<name>')
def variable(name):
    return f"hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def handle_params():
    return str(request.args)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)