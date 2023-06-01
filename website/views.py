from django.shortcuts import render
from django.http import HttpResponse
from .cucm import *
from .webex import *


def home(request):
    context = {
        "title": "Trigger python logic",
        "number": 0
    }
    return render(request, "tool.html", context)


def user(request):
    print("\nThis is the Lookup view\n")
    print("This is the request: " + str(request.POST))
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        print("This is the Username: " + username)
        cucmUser = { "userID" : username }
        devices = [ ]
        cucmUser, devices = userLookup(cucmUser, devices)
        print("devices available : " + str(devices))
        print(cucmUser)
    else:
        print("Not a POST")
    return render(request, 'user.html', {'cucmUser': cucmUser, 'devices': devices})


def webex(request):
    print("\nThis is the Webex lookup\n")
    print("This is the request: " + str(request.POST))
    if request.method == "POST":
        data = request.POST
        username = data.get("email")
        print("This is the webex Username: " + username)
        webexUser = webexLookup(username)
        webexUserCheck = webexUser['displayName']
        print("This is back in the views.py - webex()")
        print(webexUserCheck)
        if webexUserCheck == 'Nobody':
            return render(request, 'webex2.html', {'webexUser': webexUser})
        else:
            print(webexUserCheck)
    else:
        print("Not a POST")
    return render(request, 'webex.html', {'webexUser': webexUser})

def insertWebexUser(request):
    if request.method == "POST":
        data = request.POST
        accountEmail = data.get("email")
        firstName = data.get("firstName")
        lastName = data.get("lastName")
        extension = data.get("extension")
        print("This is the webex Username: " + username + firstName + lastName + extension)
        insertWebexUser = {'userEmail': accountEmail, 'firstName': firstName, 'lastName': lastName, 'extension': extension}
        newWebexUser = insertNewWebexUser(insertWebexUser)
        print("This is back in the views.py - insertWebexUser()")
        print(newWebexUser)
        print("That above is newWebexUser")
    else:
        print("Not a POST")
    return render(request, 'webex.html', {'webexUser': insertWebexUser})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
