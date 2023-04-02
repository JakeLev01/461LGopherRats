from pymongo import MongoClient
from flask import Flask, request, jsonify

app = Flask(__name__)

app.route('/addNewProject/')

def addNewProject(PersonID, Name):
    PersonID = request.args.get("PersonID")
    Name = request.args.get("Name")

    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")

    db = client['Projects']

    mycol = db.create_collection(Name)

    hw_set_1 = {'HW_set': 1, 'Capacity': 0, 'Availability': 0, 'CheckedOut': 0} 
    hw_set_2 = {'HW_set': 2, 'Capacity': 0, 'Availability': 0, 'CheckedOut': 0}

    mycol.insert_many([hw_set_1, hw_set_2])

    new_proj = {'Id': PersonID, 'Name': Name}
    mycol.insert_one(new_proj)

    client.close()

app.route("/joingProject/")

def joinProject(PersonID, Name):
    PersonID = request.args.get("PersonID")
    Name = request.args.get("Name")

    #join project and add ID to ID list
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")

    db = client['Projects']

    myproj = db[Name]

    project = myproj.find_one({'Name': Name})

    if not project:
        print('Project does not exist!')
        return

    # Add the new user to the 'users' field in the project document
    project['ID'].append(PersonID)

    # Update the project document in the collection
    myproj.update_one({'ID': Name}, {'$set': project})

    client.close()
