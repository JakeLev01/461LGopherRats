from pymongo import MongoClient
from flask import Flask, request, jsonify
import cipher

app = Flask(__name__)

##################
#SignInValidation
##################

#checks if user exists
app.route('/checkUserName/userName')
def checkUserName(userName):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']
    
    if userName in db.list_collection_names():
       return True
    else:
        return False
    

#checks if the user exists, then checks if the password is correct
app.route('/checkSignIn/<string:userID>/<string:password>')
def checkSignIn(userID, password):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        document = collection.find_one({"userID": userID}) #find userID
        if document is not None:
            DCpassword = cipher.decrypt(document.get("password"),3,1)
            if DCpassword == password:
                return "Successfuly Signed In"
            else:
                return "Password is incorrect"
            
    return "Username is not in the database"

#checks if username exists in database, create an encrypted password, then creates a new user collection
app.route("/createNewUser/<string:userID>/<string:password>/<string:Username>")
def createNewUser(userID, password, Username):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    if not checkUserName(Username):
        DCpassword = cipher.encrypt(password,3,1)
        db.create_collection(Username)
        post = {"userID": userID, "password": DCpassword}
        collection = db[Username]
        collection.insert_one(post)
        return "Account Successfully created"
    else:
        return "This userName is already taken please chose another one"

##################
#ProjectValidation
##################

#check if project already exists, adds new project
#newProject.js
app.route('/addNewProject/<string:ProjectID>/<string:Name>/<string:Description>')
def addNewProject(ProjectID, Name):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    
    if Name not in db.list_collection_names():
        mycol = db.create_collection(Name)
        hw_set_1 = {'HW_set': 1, 'Capacity': 0, 'Availability': 0, 'CheckedOut': 0}
        hw_set_2 = {'HW_set': 2, 'Capacity': 0, 'Availability': 0, 'CheckedOut': 0}
        mycol.insert_many([hw_set_1, hw_set_2])
        new_proj = {'Id': ProjectID, 'Name': Name, 'Description': "Description"}
        mycol.insert_one(new_proj)
        return "Successfully added new project"
    else:
        return "Project already exists"

#check if project already exists, join
#project.js
app.route("/joinProject/<string:ExistingID>")
def joinProject(ProjectID):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        document = collection.find_one({"ID": ProjectID})
        if document is not None:
            return "Successfully joined project"
        else:
            return "Project does not exist"



############
#HardwareSet
############

