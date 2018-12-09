from flask import request, url_for
from flask_api import FlaskAPI
from flask import jsonify
from flask import json
from flask import Response
from flask import send_from_directory, send_file
from flask_cors import CORS
import plivo
import sys
sys.path.insert(0,'/home/pi/Desktop/IntruderDetection/dbOperations')
import database

app = FlaskAPI(__name__)
CORS(app)
cassandraOperations = database.CassandraOperations()

@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    name = data['name']
    registrationStatus = registerToDB(name,'registered')
    if(registrationStatus):
        return jsonify({'result':'team registered successfully'})
    else:
        return jsonify({'result':'team is already registered'})

@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()
    teamName = data['name']
    time = data['time']
    url = data['url']
    updateDB(teamName,time,url)
    client = plivo.RestClient(auth_id='MAOTM2ZTNMOWFKZTZJYT', auth_token='OGJiMmYwNWM1NmIzN2NjMjk3YWU3M2FiOWU2NjEy')
    message_created = client.messages.create(
    src='+917892143484',
    dst='+918904655657',
    text='Intruder detected at'+time+'link: '+url)
    return jsonify({'result':'data updated successfully to cloud'})

def registerToDB(name,status):
    query = "INSERT INTO workshop.student_entries(teamName,status) values('"+name+"','"+status+"');"
    return cassandraOperations.executeQuery(query)

def updateDB(name,time,url):
    query = "UPDATE workshop.intruder_log set time='"+time+"',url='"+url+"' WHERE teamName='"+name+"';"
    return cassandraOperations.executeQuery(query)

if __name__ == '__main__':
#    cassandraOperations = database.CassandraOperations()
    cassandraOperations.createSession('192.168.1.102')
    cassandraOperations.setLogger('INFO')
    cassandraOperations.createKeyspaceIfNotExists('workshop')
    cassandraOperations.executeQuery('CREATE TABLE IF NOT EXISTS student_entries(teamName text PRIMARY KEY, status text);')
    cassandraOperations.executeQuery('CREATE TABLE IF NOT EXISTS intruder_log(teamName text PRIMARY KEY, time text, url text);')
    app.run(host='0.0.0.0', port=50010)
