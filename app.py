from pymongo import MongoClient
from flask import Flask, request, jsonify, redirect
import cipher
import os

app = Flask(__name__)

##################
#SignInValidation
##################

#checks if user exists
@app.route('/checkUserName/userName')
def checkUserName(userName):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']
    
    if userName in db.list_collection_names():
       return True
    else:
        return False
    

#checks if the user exists, then checks if the password is correct
@app.route('/checkSignIn/<string:userID>/<string:password>')
def checkSignIn(userID, password):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        document = collection.find_one({"userID": userID}) #find userID
        if document is not None:
            DCpassword = cipher.decrypt(document.get("password"),3,1)
            if DCpassword == password:
                return "Successfully Signed In"
            else:
                return "Password is incorrect"
            
    return "Username is not in the database"

#checks if username exists in database, create an encrypted password, then creates a new user collection
@app.route("/createNewUser/<string:userID>/<string:password>/<string:Username>")
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
global_project_id = ""
@app.route('/addNewProject/<string:ProjectID>/<string:Name>/<string:Description>')
def addNewProject(ProjectID, Name, Description):
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

#check if project already exists, join
#project.js
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
#HardwareSet
############

#gets projectid, input quantity, and which HWset-> then updates database values, and return the new availability
@app.route('/check_out/<string:projectID>/<int:qty>/<int:HWset>')
def check_out(projectID, qty, HWSet):

    HWSetAvailability = 0
    CheckedOut = 0
    global collection
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()

    #gets data from database
    for col in cols:
        doc = col.find()
        if doc.get('Id') == projectID:
            collection = col
            if HWSet == 1:
                hw_set_doc = collection.find_one({'HW_set': 1})
                HWSetAvailability = hw_set_doc['Availability']
                CheckedOut = hw_set_doc['CheckedOut']
            elif HWSet == 2:
                hw_set_doc = collection.find_one({'HW_set': 2})
                HWSetAvailability = hw_set_doc['Availability']
                CheckedOut = hw_set_doc['CheckedOut']
        break

    if qty < 0:
        return "Invalid Quantity"
    elif qty > HWSetAvailability:
        CheckedOut += HWSetAvailability
        HWSetAvailability = 0
    else:
        HWSetAvailability -= qty
        CheckedOut += qty

    #updates database
    if HWSet == 1:
        collection.update_one({"HW_set": 1}, {"$set": {"Availability": HWSetAvailability}}, {"set": {"CheckedOut": CheckedOut}})
    elif HWSet == 2:
        collection.update_one({"HW_set": 2}, {"$set": {"Availability": HWSetAvailability}}, {"set": {"CheckedOut": CheckedOut}})

    response = {'availability': HWSetAvailability, 'checkedout': CheckedOut}
    return jsonify(response)


#gets projectid, input quantity, and which HWset-> then updates database values, and return the new availability
@app.route('/check_in/<string:projectID>/<int:qty>/<int:HWset>')
def check_in(projectID, qty, HWSet):

    HWSetAvailability = 0
    CheckedOut = 0
    Capacity = 0
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()
    global collection

    for col in cols:
        doc = col.find()
        if doc.get('ProjectID') == projectID:
            collection = col
            if HWSet == 1:
                hw_set_doc = collection.find_one({'HW_set': 1})
                HWSetAvailability = hw_set_doc['Availability']
                CheckedOut = hw_set_doc['CheckedOut']
            elif HWSet == 2:
                hw_set_doc = collection.find_one({'HW_set': 2})
                HWSetAvailability = hw_set_doc['Availability']
                CheckedOut = hw_set_doc['CheckedOut']
        break


    if qty < 0:
        return "Invalid Quantity"
    elif (qty > Capacity) or (qty + HWSetAvailability) > Capacity:
        updateCheckOut = Capacity - HWSetAvailability
        CheckedOut -= updateCheckOut
        HWSetAvailability = Capacity
    else:
        HWSetAvailability += qty
        CheckedOut -= qty
        
    #updates database
    if HWSet == 1:
        collection.update_one({"HW_set": 1}, {"$set": {"Availability": HWSetAvailability}}, {"set": {"CheckedOut": CheckedOut}})
    elif HWSet == 2:
        collection.update_one({"HW_set": 2}, {"$set": {"Availability": HWSetAvailability}}, {"set": {"CheckedOut": CheckedOut}})

    response = {'availability': HWSetAvailability, 'checkedout': CheckedOut}
    return jsonify(response)

@app.route('/getProjectID')
def getProjectID():
    return global_project_id

@app.route('/getProject/<int:projectID>')
def getProject(projectID):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()
    for col in cols:
        doc = col.find()
        if doc.get('ProjectID') == projectID:
            post = {"ProjectID": doc.get('ProjectID'), "HWSet1Availability": doc.get('HWSet1Availability'),
                    "HWSet2Availability": doc.get('HWSet1Availability'), "Capacity": doc.get('Capacity'),
                    "HWSet1Checked Out": doc.get('HWSet1CheckedOut'), "HWSet2Checked Out": doc.get('HWSet2CheckedOut')}
            return jsonify(post)

    return "Invalid projectID"

############
#Redirect
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
    app.run(debug= True,host='0.0.0.0', port=os.environ.get("PORT", 5000))