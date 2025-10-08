from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path='/')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/static_bootstrap')
def static_bootstrap():
    return render_template("static_bootstrap.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)