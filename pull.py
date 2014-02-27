#!/usr/bin/env python

import synapseclient
import os.path

configuration = '/home/boiseb01/.synapse-key.txt'

if not os.path.isfile(configuration):
	print("Error: " + configuration + " is not a file")
	sys.exit(1)

#print("DEBUG configuration " + configuration)

reader = open(configuration)

key1= reader.readline().strip()
key2 = reader.readline().strip()

#print("DEBUG attempting login with " + key1)

synapse = synapseclient.login(key1, key2)
#synapse = synapseclient.login()

print("DEBUG Got connection to synapse")

handles = []
handles.append("syn2343226")
handles.append("syn2343245")
handles.append("syn2344779")
handles.append("syn2342038")
#~/.synapse-key.txt

mustDownload = True
location = "."

for handle in handles:
	entity = synapse.get(handle, downloadFile = mustDownload, downloadLocation = location)
	print("Handle: " + handle)
	print(" Name: " + entity.name)
	print(" Path: " + entity.path)
