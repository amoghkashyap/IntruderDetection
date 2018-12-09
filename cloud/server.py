from flask import request, url_for
from flask_api import FlaskAPI
from flask import jsonify
from flask import json
from flask import Response
from flask import send_from_directory, send_file
from flask_cors import CORS
import plivo

app = FlaskAPI(__name__)
CORS(app)

@app.route('/register',methods=['POST'])
def processjson():
    data = request.get_json()
    print(data)
    name = data['name']
    print (name)
    client = plivo.RestClient(auth_id='MAOTM2ZTNMOWFKZTZJYT', auth_token='OGJiMmYwNWM1NmIzN2NjMjk3YWU3M2FiOWU2NjEy')
    message_created = client.messages.create(
    src='+917892143484',
    dst='+918904655657',
    text='Team '+name+' registered successfully')
    return jsonify({'result':'team registered successfully'})

@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()
    print(data)
    return jsonify({'result':'data updated successfully to cloud'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50010)
