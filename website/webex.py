from dotenv.main import load_dotenv
import os
import requests
import json


def webexLookup(accountEmail):
    # Load environmental variables from .dev file
    load_dotenv()

    print("inside WebexLookup")

    # Basic Variables setup - taken from .env file
    apiUrl = os.environ['WEBEXAPIURLLISTPEOPLE']
    apiUrls = apiUrl + accountEmail
    access_token = os.environ['ACCESSTOKEN']

    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    # queryParams = { 'sortBy': 'lastactivity', 'max': '2' } , params = queryParams

    r = requests.get( url = apiUrls, headers = httpHeaders)
    rootJson = r.json()
    print(rootJson)
    # Let's check if the JSON string returned has a valid user - If true, we have NO user.
    validJson = len(rootJson['items'])
    if validJson == 0 :
        print("nothing to see here")
        webexUser = {'displayName': 'Nobody', 'email': accountEmail}

    else:
        print(rootJson)
        print(len(rootJson['items']))
        displayName = rootJson['items'][0]['displayName']
        firstName = rootJson['items'][0]['firstName']
        lastName = rootJson['items'][0]['lastName']
        lastModified = rootJson['items'][0]['lastModified']
        #Not all users have logged in before - If they have never, this will generate error
        try:
            lastActivity = rootJson['items'][0]['lastActivity']
        except:
            lastActivity = "Never Logged In"

        #Not all users have extensions - If they don't have, this will generate error
        try:
            extension = rootJson['items'][0]['phoneNumbers'][0]['value']
        except:
            extension = ""

        try:
            avatar = rootJson['items'][0]['avatar']
        except:
            avatar = "/static/images/noAvatar.png"
        webexUser = {'userEmail': accountEmail,'displayName': displayName, 'firstName': firstName, 'lastName': lastName, 'extension': extension, 'lastActivity': lastActivity, 'lastModified': lastModified, 'avatar': avatar}

    return webexUser

def insertNewWebexUser(insertWebexUser):
    # Load environmental variables from .dev file
    load_dotenv()

    print("inside insertWebexUser")
    print(insertWebexUser)
    # Basic Variables setup - taken from .env file
    apiUrl = os.environ['WEBEXAPIURLINSERTPEOPLE']
    access_token = os.environ['ACCESSTOKEN']
    orgID = os.environ['ORGID']

    newUserEmail = insertWebexUser.get('userEmail')
    newUserExtension = insertWebexUser['extension']
    newUserFirstName = insertWebexUser['firstName']
    newUserLastName = insertWebexUser['lastName']

    token = 'Bearer '+access_token

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }

    data = json.dumps({
        "emails": [
            newUserEmail
        ],
        "phoneNumbers": [
            {
                "type": "work",
                "value": newUserExtension
            }],
        "firstName": newUserFirstName,
        "lastName": newUserLastName,
    })

    datax = {
            "emails": [newUserEmail],
        }
    print("This is Headers")
    print(headers)
    print("This is Data")
    print(data)
    print("data end")
#    response = requests.post(url=apiUrl, headers=headers, data=data)

    response = requests.request("POST", apiUrl, headers=headers, data=data)
    print(response)

    return response