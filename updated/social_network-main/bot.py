import os
import json
import requests
import re

BASE_URL="http://localhost:8000"

## User Sign up
while True:
    first_name = input('Enter first name')
    if first_name:
        break
    else:
        print('First Name field cant be empty:Try again')
while True:
    last_name = input('Enter last name')
    if last_name:
        break
    else:
        print('Last Name field cant be empty:Try again')
while True:
    email = input('Enter email')
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email and (re.fullmatch(regex, email)):
        break
    else:
        print('Enter valid Email')
while True:
    password = input('Enter password')
    if password:
        break
    else:
        print('Password field cant be empty:Try again')
url = f"{BASE_URL}/api/sign-up"
data = {"first_name":first_name,"last_name":last_name,"email":email,"username":email,"password":password}
response = requests.post(url,data = data)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
    response.raise_for_status()



## For Login User
print('Enter your email & password to Log-in')
while True:
    email = input('enter email')
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email and (re.fullmatch(regex, email)):
        break
    else:
        print('Enter valid Email')
while True:
    password = input('enter password')
    if password:
        break
    else:
        print('Password field cant be empty:Try again')
url = f"{BASE_URL}/api/token/"
data = {"username":email,"password":password}
response = requests.post(url,data =data)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key)
    access_token= jData[key]
    print(access_token)
else:
	print('Enterd data did not match to any User')
	response.raise_for_status()



## For Post creation
print('Create your post here')
while True:
    title = input("Enter Post Title: ")
    if title:
        break
    else:
        print('title field cant be empty:Try again')
description = input("Enter description: ")
url = f"{BASE_URL}/api/post"
data = {"title":title,"description":description}
headers = {"Authorization":f"Bearer {access_token}"}
response = requests.post(url,data = data,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	print('Enterd data did not match to any User')
	response.raise_for_status()



## For Viewing all posts]
print('These are all your posts')
url = f"{BASE_URL}/api/post"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.get(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    for key in jData:
        print(key,jData[key])
else:
    response.raise_for_status()



## For Like/Dislike Post
print('Like/Dislike post according to its post id')

while True:
    post = input("Enter post id ")
    try:
        val = int(post)
        break;
    except ValueError:
        print("Please enter a valid id")
url = f"{BASE_URL}/api/like-dislike"
headers = {'Authorization':f'Bearer {access_token}'}
data = {
    "post":post
}
response = requests.post(url,data = data,headers = headers)
if(response.ok):
	jData = json.loads(response.content)
	print("The response contains {0} properties".format(len(jData)))
	print("\n")
	for key in jData:
		print(key,jData[key])
else:
	response.raise_for_status()



## For viewing single user post
print('View post according to its post id')
while True:
    params = input("Enter post id ")
    try:
        val = int(params)
        break;
    except ValueError:
        print("Please enter a valid id")

url = f"{BASE_URL}/api/post/{params}"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.get(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	response.raise_for_status()


## For Delete post
print('Delete post according to its post id')
while True:
    params = input("Enter post id ")
    try:
        val = int(params)
        break;
    except ValueError:
        print("Please enter a valid id")
url = f"{BASE_URL}/api/post/{params}"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.delete(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	response.raise_for_status()

