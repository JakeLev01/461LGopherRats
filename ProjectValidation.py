from pymongo import MongoClient
from flask import Flask, jsonify


def addNewProject(PersonID, Name):

    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")

    db = client['Projects']

    mycol = db.create_collection(Name)

    new_proj = {'Id': PersonID, 'Name': Name}
    mycol.insert_one(new_proj)

    client.close()

def joinProject(PersonID, Name):

    #join project and add ID to ID list
    client = MongoClient("mongodb+srv://jakeleverett:<password>@cluster0.ikaumwm.mongodb.net/test")

    db = client['Projects']

    myproj = db[Name]

    project = myproj.find_one({'Name': Name})

    # Add the new user to the 'users' field in the project document
    project['ID'].append(PersonID)

    # Update the project document in the collection
    myproj.update_one({'ID': Name}, {'$set': project})

    client.close()