from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': 'Ivar Aasen',
        'age': 18
    },
    {
        'id': 2,
        'name': 'Olga Ola Helge Persson III',
        'age': 87
    },
    {
        'id': 3,
        'name': 'Anders Petter Anderson',
        'age': 'aAa presis'
    }
]

@app.route('/api/contacts')
def getContacts(): 
    return jsonify(contacts)

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