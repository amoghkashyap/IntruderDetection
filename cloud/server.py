from flask import request, url_for
from flask_api import FlaskAPI
from flask import jsonify
from flask import json
from flask import Response
from flask import send_from_directory, send_file
from flask_cors import CORS

app = FlaskAPI(__name__)
CORS(app)

@app.route('/register',methods=['POST'])
def processjson():
    data = request.get_json()
    print(data)
    return jsonify({'result':'team registered successfully'})

@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()
    print(data)
    return jsonify({'result':'data updated successfully to cloud'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50010)
