from pymongo import MongoClient

def insertCollection(projectName, projectId, projectDescription):
    client = MongoClient("mongodb+srv://jakeleverett:rOxNEdt5txSolGvm@cluster0.ikaumwm.mongodb.net/test")
    db = client["Projects"]
    db.create_collection(projectName)
    Name = projectName
    ID = projectId
    Description = projectDescription
    post = {"Name": Name, "ID": ID, "Description": Description}
    collection = db[projectName]
    collection.insert_one(post)
    client.close()


insertCollection("Project Test", "jsl3356", "This is a test project")