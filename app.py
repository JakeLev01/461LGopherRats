from pymongo import MongoClient
from flask import Flask, request, jsonify, redirect
import cipher
import os

app = Flask(__name__)


##################
# SignInValidation
##################

# checks if user exists
@app.route('/checkUserName/userName')
def checkUserName(userName):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    if userName in db.list_collection_names():
        return True
    else:
        return False


# checks if the user exists, then checks if the password is correct
@app.route('/checkSignIn/<string:userID>/<string:password>')
def checkSignIn(userID, password):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        document = collection.find_one({"userID": userID})  # find userID
        if document is not None:
            DCpassword = cipher.decrypt(document.get("password"), 3, 1)
            if DCpassword == password:
                return "Successfully Signed In"
            else:
                return "Password is incorrect"

    return "Username is not in the database"


# checks if username exists in database, create an encrypted password, then creates a new user collection
@app.route("/createNewUser/<string:userID>/<string:password>/<string:Username>")
def createNewUser(userID, password, Username):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    if not checkUserName(Username):
        DCpassword = cipher.encrypt(password, 3, 1)
        db.create_collection(Username)
        post = {"userID": userID, "password": DCpassword}
        collection = db[Username]
        collection.insert_one(post)
        return "Account Successfully created"
    else:
        return "This userName is already taken please choose another one"


##################
# ProjectValidation
##################

global_project_id = ""
@app.route('/addNewProject/<string:ProjectID>/<string:Name>/<string:Description>')
def addNewProject(ProjectID, Name, Description):
    print("hey")
    global global_project_id
    global_project_id = ProjectID
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']

    if Name not in db.list_collection_names():
        mycol = db.create_collection(Name)
        hw_set_1 = {'HW_set': 1, 'Capacity': 100, 'Availability': 100, 'CheckedOut': 0}
        hw_set_2 = {'HW_set': 2, 'Capacity': 100, 'Availability': 100, 'CheckedOut': 0}
        mycol.insert_many([hw_set_1, hw_set_2])
        new_proj = {'Id': ProjectID, 'Description': Description}
        mycol.insert_one(new_proj)
        return "Successfully added new project"
    else:
        return "Project already exists"


# check if project already exists, join
# project.js
@app.route("/joinProject/<string:ProjectID>")
def joinProject(ProjectID):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']

    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        document = collection.find_one({"Id": ProjectID})
        if document is not None:
            return "Successfully joined project"

    return "Project does not exist"


############
# HardwareSet
############

#gets projectid, input quantity, and which HWset-> then updates database values, and return the new availability
@app.route('/check_out/<string:projectID>/<int:qty>/<int:HWset>')
def check_out(projectID, qty, HWset):

    HWSetAvailability = 0
    CheckedOut = 0
    message = "Successfully Checked-out"
    global collection
    global doc
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()

    #gets data from database
    for col in cols:
        collection = db[col]
        doc = collection.find_one({'Id': projectID})
        if doc is not None:
            if doc['Id'] == projectID:
                if HWset == 1:
                    hw_set_doc = collection.find_one({'HW_set': 1})
                    HWSetAvailability = hw_set_doc['Availability']
                    CheckedOut = hw_set_doc['CheckedOut']
                elif HWset == 2:
                    hw_set_doc = collection.find_one({'HW_set': 2})
                    HWSetAvailability = hw_set_doc['Availability']
                    CheckedOut = hw_set_doc['CheckedOut']
                break

    if qty < 0:
        response = {'message': "Invalid Quantity"}
        return jsonify(response)
    elif qty > HWSetAvailability:
        CheckedOut += HWSetAvailability
        HWSetAvailability = 0
        message = "Unable to checkout entire quantity"
    else:
        HWSetAvailability -= qty
        CheckedOut += qty

    #updates database
    if HWset == 1:
        collection.update_one({"HW_set": 1}, {"$set": {"Availability": HWSetAvailability, "CheckedOut": CheckedOut}}, upsert=False)
    elif HWset == 2:
        collection.update_one({"HW_set": 2}, {"$set": {"Availability": HWSetAvailability, "CheckedOut": CheckedOut}}, upsert=False)

    response = {'availability': HWSetAvailability, 'checkedout': CheckedOut, 'message': message}
    return jsonify(response)


#gets projectid, input quantity, and which HWset-> then updates database values, and return the new availability
@app.route('/check_in/<string:projectID>/<int:qty>/<int:HWset>')
def check_in(projectID, qty, HWset):

    HWSetAvailability = 0
    CheckedOut = 0
    Capacity = 100
    message = "Successfully Checked-in"
    global collection
    global doc
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()

    # gets data from database
    for col in cols:
        collection = db[col]
        doc = collection.find_one({'Id': projectID})
        if doc is not None:
            if doc['Id'] == projectID:
                if HWset == 1:
                    hw_set_doc = collection.find_one({'HW_set': 1})
                    HWSetAvailability = hw_set_doc['Availability']
                    CheckedOut = hw_set_doc['CheckedOut']
                elif HWset == 2:
                    hw_set_doc = collection.find_one({'HW_set': 2})
                    HWSetAvailability = hw_set_doc['Availability']
                    CheckedOut = hw_set_doc['CheckedOut']
                break

    if qty < 0:
        response = {'message': "Invalid Quantity"}
        return jsonify(response)
    elif (qty > Capacity) or (qty + HWSetAvailability) > Capacity:
        updateCheckOut = Capacity - HWSetAvailability
        CheckedOut -= updateCheckOut
        HWSetAvailability = Capacity
        message = "Unable to check in entire quantity"
    else:
        HWSetAvailability += qty
        CheckedOut -= qty

    # updates database
    if HWset == 1:
        collection.update_one({"HW_set": 1}, {"$set": {"Availability": HWSetAvailability, "CheckedOut": CheckedOut}}, upsert=False)
    elif HWset == 2:
        collection.update_one({"HW_set": 2}, {"$set": {"Availability": HWSetAvailability, "CheckedOut": CheckedOut}}, upsert=False)

    response = {'availability': HWSetAvailability, 'checkedout': CheckedOut, 'message': message}
    return jsonify(response)


@app.route('/getProject/<string:projectID>')
def getProject(projectID):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()
    for col in cols:
        collection = db[col]
        doc = collection.find_one({'Id': projectID})
        if doc is not None:
            if doc['Id'] == projectID:
                hw_set_1_doc = collection.find_one({'HW_set': 1})
                hw_set_2_doc = collection.find_one({'HW_set': 2})
                post = {"HWSet1Availability": hw_set_1_doc['Availability'],
                    "HWSet2Availability":hw_set_2_doc['Availability'],
                    "HWSet1CheckedOut": hw_set_1_doc['CheckedOut'], 
                    "HWSet2CheckedOut": hw_set_2_doc['CheckedOut']}
            return jsonify(post)

    return "Invalid projectID"


############
# Redirect
############

@app.route('/resourceRedirect')
def resourceRedirect():
    return redirect('/resources')


@app.route('/signInRedirect')
def signInRedirect():
    return redirect('/signIn')


@app.route('/newProjectRedirect')
def newProjectRedirect():
    return redirect('/newProject')


@app.route('/projectRedirect')
def projectRedirect():
    return redirect('/project')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=os.environ.get("PORT", 5000))
