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
app.route('/addNewProject/')
def addNewProject(PersonID, Name):
    PersonID = request.args.get("PersonID")
    Name = request.args.get("Name")

    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")

    db = client['Projects']

    mycol = db.create_collection(Name)

    new_proj = {'Id': PersonID, 'Name': Name}
    mycol.insert_one(new_proj)

    client.close()

#join project and add user id to database
app.route("/joinProject/<string:ExistingID/<string:Name>")
def joinProject(PersonID, Name):

    #join project and add ID to ID list
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")

    db = client['Projects']

    myproj = db[Name]

    project = myproj.find_one({'Name': Name})

    # Add the new user to the 'users' field in the project document
    project['ID'].append(PersonID)

    # Update the project document in the collection
    myproj.update_one({'ID': Name}, {'$set': project})

    client.close()


############
#HardwareSet
############

