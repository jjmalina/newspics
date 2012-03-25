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

print pyObj['response'][0]
i=0
for each in pyObj['response']:
    if (each['type'] == 'photo'):
#	print len(each['photos'])
	for i in range(len(each['photos'])):
            print each['photos'][0]['original_size']['url']
#            if (each['photos'][i] == 'original_size'):
            #j    print each['photos'][i]
             #   print 'hey there'
           # elif (each['photos'][i] == 'caption'):
           #     print each['photos'][i]
           #     print 'hello'
           # else:
           #     print each['photos'][i] 
           #     print 'hi'
#    print each['tags']
#    print each['tags'][0]
    #for i in range(len(pyObj['response'])): #        if (each[i] == 'url'):
    #    print each[i 
#for each in pyObj['alt_sizes']:
#	print each
#	print each['type']
#take gifs from now python object and make a submission to database.
