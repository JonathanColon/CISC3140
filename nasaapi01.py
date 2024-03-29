﻿
# Importing required python3 libraries 

#!/usr/bin/env python3
import urllib.request
import json
import webbrowser

#Define APOD and set the key

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=DEMO_KEY'

#Calls the Webservice

apodurlobj = urllib.request.urlopen(apodurl + mykey)

#Reads the file object in JSON

apodread = apodurlobj.read()

#prints JSON version of the file

print(apodread)

#Decodes JSON to python data structure

decodeapod = json.loads(apodread.decode('utf-8'))

#Displays python data in readable format

print("\n\nConverted python data")
print(decodeapod)

#displays NASA picture of the day in a webbrowser

input('\nPress enter to open NASA picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])