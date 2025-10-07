from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/')
def index():
    myName = "Roman Nihal"
    myAge = 20+4
    # return render_template("index.html", myName=myName, myAge=myAge)
    myList = [11, 22, 33, 44, 55]
    return render_template("index.html", list=myList)

@app.route('/filters')
def filters():
    name = "Roman Nihal"
    return render_template("filters.html", name=name)

@app.route('/redirect_')
def redirect_():
    return redirect(url_for("filters"))

@app.template_filter("reverse_string")
def reverse_string(s):
    return s[::-1]

@app.template_filter("repeat")
def repeat(s, times=1):
    return s * times


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)