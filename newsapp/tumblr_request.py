#!/usr/bin/env python

import json
import requests
import settings
import sys

#accept an argument
if(len(sys.argv) > 1):
    SearchObj= sys.argv[1]
else:
    SearchObj = 'mountains'

obj = requests.get('http://api.tumblr.com/v2/tagged?tag='+ SearchObj + '&api_key=' + settings.TUMBLR_KEY)

#convert obj(JSON) to a python object.
pyObj = json.loads(obj.text)

i=0
for each in pyObj['response']:
    if (each['type'] == 'photo'):
	for i in range(len(each['photos'])):
