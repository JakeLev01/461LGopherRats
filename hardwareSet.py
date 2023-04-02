from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

app.route('/check_out')
def check_out(projectID, qty, HWSet):
    projectID = request.args.get("projectID")
    qty = request.args.get("qty")
    HWSet = request.args.get("HWSet")

    HWSetAvailability = 0
    CheckedOut = 0
    global collection
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client['Projects']
    cols = db.list_collection_names()

    for col in cols:
        doc = col.find()
        if doc.get('ProjectID') == projectID:
            collection = col
            if HWSet == 1:
                HWSetAvailability = doc.get("HWSet1Availability")
                CheckedOut = doc.get('HWSet1CheckedOut')
            elif HWSet == 2:
                HWSetAvailability = doc.get("HWSet2Availability")
                CheckedOut = doc.get('HWSet2CheckedOut')
        break

    if qty < 0:
        return "Invalid Quantity"
    elif qty > HWSetAvailability:
        CheckedOut += HWSetAvailability
        HWSetAvailability = 0
        if HWSet == 1:
            post = {"HWSet1Availability": HWSetAvailability, "HWSet1CheckedOut": CheckedOut}
            db[collection].update_one(post)
        elif HWSet == 2:
            post = {"HWSet2Availability": HWSetAvailability, "HWSet2CheckedOut": CheckedOut}
            db[collection].update_one(post)
        return
    else:
        HWSetAvailability -= qty
        CheckedOut += qty
        if HWSet == 1:
            post = {"HWSet1Availability": HWSetAvailability, "HWSet1CheckedOut": CheckedOut}
            db[collection].update_one(post)
        elif HWSet == 2:
            post = {"HWSet2Availability": HWSetAvailability, "HWSet2CheckedOut": CheckedOut}
            db[collection].update_one(post)

        return 0


app.route('/check_in')
def check_in(projectID, qty, HWSet):
    projectID = request.args.get("projectID")
    qty = request.args.get("qty")
    HWSet = request.args.get("HWSet")

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
                HWSetAvailability = doc.get("HWSet1Availability")
                CheckedOut = doc.get('HWSet1CheckedOut')
            elif HWSet == 2:
                HWSetAvailability = doc.get("HWSet2Availability")
                CheckedOut = doc.get('HWSet2CheckedOut')
            Capacity = doc.get('Capacity')
        break


    if qty < 0:
        return "Invalid Quantity"
    elif (qty > Capacity) or (qty + HWSetAvailability) > Capacity:
        updateCheckOut = Capacity - HWSetAvailability
        CheckedOut -= updateCheckOut
        HWSetAvailability = Capacity
        if HWSet == 1:
            post = {"HWSet1Availability": HWSetAvailability, "HWSet1CheckedOut": CheckedOut}
            db[collection].update_one(post)
        elif HWSet == 2:
            post = {"HWSet2Availability": HWSetAvailability, "HWSet2CheckedOut": CheckedOut}
            db[collection].update_one(post)
    else:
        HWSetAvailability += qty
        CheckedOut -= qty
        if HWSet == 1:
            post = {"HWSet1Availability": HWSetAvailability, "HWSet1CheckedOut": CheckedOut}
            db[collection].update_one(post)
        elif HWSet == 2:
            post = {"HWSet2Availability": HWSetAvailability, "HWSet2CheckedOut": CheckedOut}
            db[collection].update_one(post)



app.route('/getProject/<int:projectID>')
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
