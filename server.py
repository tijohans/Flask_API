from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)


client = MongoClient(os.getenv('DB_CONNECTION'))
db = client.contact_db

collection = db.contacts

contacts = []

@app.route('/api/contacts')
def getContacts(): 
    return ''

@app.route('/api/contacts', methods=['POST'])
def createContact():
    newContact = {
        'name': request.json['name'],
        'age': request.json['age']
    }
    contacts.append(newContact)
    return contacts

@app.route('/api/contacts/<id>', methods=['PUT'])
def updateContact(id):
    for contact in contacts:
        if not contact['id'] == int(id):
            continue
        
        contact['name'] = request.json['name']
        contact['age'] = request.json['age']
        return contact

@app.route('/api/contacts/<id>', methods=['DELETE'])
def deleteContact(id):
    for index, contact in enumerate(contacts):
        if not contact['id'] == int(id):
            continue
            
        contacts.pop(index)
        return contact
        
@app.route('/api/contacts/<id>')
def getContact(id):
    for contact in contacts:
        if contact['id'] == int(id):
            return contact    
    return {'message': 'Contact with id: ' + id + ' not found'}


app.run()