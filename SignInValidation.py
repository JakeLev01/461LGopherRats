from pymongo import MongoClient
import cipher

def checkUserName(userName):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']
    for x in db.find():
        if userName == x.get("userID"):
            return True

    return False

def checkSignIn(userName, password):
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

def createNewUser(userName, password):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Users']

    if(checkUserName(userName)):
        DCpassword = cipher.encrypt(password,3,1)
        db.create_collection(userName)
        post = {"userID": userName, "password": DCpassword}
        collection = db[userName]
        collection.insert_one(post)
        return "Account Successfully created"
    else:
        return "This userName is already taken please chose another one"