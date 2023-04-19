import app
import pytest_check as check

def testCheckUserName():
    userID = 'charu1'
    response = app.checkUserName(userID)
    assert response == True

    userID = 'FakeUser'
    response = app.checkUserName(userID)
    assert response == False

def testCheckSignIn():
    userID = 'charu1'
    password = 'hello'
    response = app.checkSignIn(userID,password)
    assert response == "Successfully Signed In"

    password = 'wrongPassword'
    response = app.checkSignIn(userID,password)
    assert response == "Password is incorrect"

    userID = 'FakeUser'
    response = app.checkSignIn(userID,password)
    assert response == "Username is not in the database"

def testCreateNewUser():
    userID = 'charu1'
    password = 'hello'
    username = 'charu1'
    response = app.createNewUser(userID,password,username)
    assert response == "Account Successfully created"

    userID = 'jessie'
    response = app.createNewUser(userID,password,username)
    assert response == "This userName is already taken please choose another one"

def testAddNewProject():
    projectID = 'test'
    Name = 'Test Project 1'
    Description = 'This is a test of the Add New Project Function'
    response = app.addNewProject(projectID,Name,Description)
    assert response == "Successfully added new project"

    Name = 'hello'
    response = app.addNewProject(projectID,Name,Description)
    assert response == "Project already exists"

def testJoinProject():
    projectID = 'jake'
    response = app.joinProject(projectID)
    assert response == "Successfully joined project"

    projectID = 'fake'
    response = app.joinProject(projectID)
    assert response == "Project does not exist"

def testCheckOut():
    projectID = 'project12'
    qty = 23
    HWSet = 2
    response = app.check_out(projectID,qty,HWSet)
    assert response['message'] == "Successfully Checked Out Hardware!"

    qty= -2
    response = app.check_out(projectID,qty,HWSet)
    assert response['message'] == "Invalid Quantity"

    qty= 110
    response = app.check_out(projectID,qty,HWSet)
    assert response['message'] == "Unable to checkout entire quantity"

def testCheckIn():
    projectID = 'project12'
    qty = 12
    HWSet = 1
    response = app.check_in(projectID,qty,HWSet)
    assert response['message'] == "Successfully Checked In Hardware!"

    qty= -2
    response = app.check_in(projectID,qty,HWSet)
    assert response['message'] == "Invalid Quantity"

    qty= 110
    response = app.check_in(projectID,qty,HWSet)
    assert response['message'] == "Unable to checkout entire quantity"

def testGetProject():
    projectID = '1'
    response = app.getProject(projectID)
    assert response != "Invalid projectID"
    
    projectID = 'fake'
    response = app.getProject(projectID)
    assert response == "Invalid projectID"