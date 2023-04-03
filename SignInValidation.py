from pymongo import MongoClient
from flask import Flask, request, jsonify
import cipher

app = Flask(__name__)

app.route('/checkUserName/userName')
def checkUserName(userName):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']
    for x in db.find():
        if userName == x.get("userID"):
            return True

    return False

<<<<<<< Updated upstream
<<<<<<< Updated upstream
app.route('/checkSignIn/')
=======
#check username, grab pwd and compare it
>>>>>>> Stashed changes
=======
#check username, grab pwd and compare it
>>>>>>> Stashed changes
def checkSignIn(userName, password):
    userName = request.args.get("userName")
    password = request.args.get("password")
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    for x in db.find():
        if userName == x.get("userID"):
            DCpassword = cipher.decrypt(x.get("password"),3,1)
            if DCpassword == password:
                return True
            else:
                return "Credentials are incorrect"

    return "Username is not in the database"

<<<<<<< Updated upstream
<<<<<<< Updated upstream
app.route("/createNewUser/")
=======
#check if user in database, and add it
>>>>>>> Stashed changes
=======
#check if user in database, and add it
>>>>>>> Stashed changes
def createNewUser(userName, password):
    userName = request.args.get("userName")
    password = request.args.get("password")
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    if checkUserName(userName):
        DCpassword = cipher.encrypt(password,3,1)
        db.create_collection(userName)
        post = {"userID": userName, "password": DCpassword}
        collection = db[userName]
        collection.insert_one(post)
        return "Account Successfully created"
    else:
        return "This userName is already taken please chose another one"
