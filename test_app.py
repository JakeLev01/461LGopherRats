import app
import pytest_check as check


def testCheckIn():
    projectID = "project12"
    qty = 12
    HWSet = 1
    response = app.check_in(projectID,qty,HWSet)
    assert response['message'] == "Successfully Checked In Hardware!"

def testCheckOut():
    projectID = 'project12'
    qty = 23
    HWSet = 2
    response = app.check_out(projectID,qty,HWSet)
    assert response['message'] == "Successfully Checked Out Hardware!"

def testJoinProject():
    projectID = 'jake'
    response = app.joinProject(projectID)
    assert response == "Successfully joined project"

def testAddNewProject():
    projectID = 'hello'
    Name = 'Test Project 1'
    Description = 'This is a test of the Add New Project Function'
    response = app.addNewProject(projectID,Name,Description)
    assert response == "Successfully added new project"

def testCreateNewUser():
    userID = 'charu1'
    password = 'hello'
    username = 'charu1'
    response = app.createNewUser(userID,password,username)
    assert response == "Account Successfully created"

def testCheckSignIn():
    userID = 'charu1'
    password = 'hello'
    response = app.checkSignIn(userID,password)
    assert response == "Successfully Signed In"

def testCheckUserName():
    userID = 'charu1'
    response = app.checkUserName(userID)
    assert response == True

def testGetProject():
    projectID = 'project12'
    response = app.getProject(projectID)
    assert response != "Invalid projectID"