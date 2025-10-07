from flask import Flask, render_template, request, send_file, Response, jsonify
import os, uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "Started flask"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_file.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'Roman' and password == "1234":
            return "Success"
        else:
            return "Failed"
    else:
        return ""
    
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files.get('file')
    filename = f"{uuid.uuid4()}.pdf"
    if not file or file.filename == '':
        return "No file selected", 400

    if file.content_type == "application/pdf":
        file_path = os.path.join(UPLOAD_FOLDER, str(filename))
        file.save(file_path)
        return send_file(file_path, mimetype='application/pdf')
    else:
        return "Unsupported file type", 400
    
@app.route('/file_download', methods=['POST'])
def file_download():
    file = request.files.get('file')
    if not file or file.filename == '':
        return "No file selected", 400
    
    file_path = os.path.join(UPLOAD_FOLDER, str(file.filename))
    file.save(file_path)

    return send_file(
        file_path,
        as_attachment=True,
        download_name="download.pdf",
        mimetype='application/pdf'
    )
    
    # with open(file_path, 'rb') as f:
    #     file_data = f.read()

    # response = Response(file_data, mimetype='application/pdf')
    # response.headers['Content-Disposition'] = f'attachment; filename="download.pdf"'

    # return response

@app.route("/handle_post", methods=["POST"])
def handle_post():
    data = request.get_json()

    if not data or "message" not in data or "name" not in data:
        return jsonify({"error": "Missing 'name' or 'message'"}), 400

    name = data["name"].strip()
    message = data["message"].strip()

    file_path = os.path.join(UPLOAD_FOLDER, "file.txt")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{name}, {message}\n")

    return jsonify({"response": "successful"}), 200

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)