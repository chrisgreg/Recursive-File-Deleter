#!/usr/bin/python

#Recursive File Deleter
#Author: Chris Gregori
#Date: 12/02/13

import os
import sys
import time

# Variables
path = sys.argv[1] # e.g. "/Users/chrisgregori/Downloads/"
fileType = sys.argv[2] # e.g ".mp3"
deletedList = []
count = 0

# Check for log request
if len(sys.argv) >= 4:
	if sys.argv[3].lower() == 'log':
         logFiles = True

# Loop to delete Files
for root, subFolders, files in os.walk(path):
	for fileName in files:
		if fileType in fileName:
			os.remove(os.path.join(root, fileName))
			count += 1
			if logFiles:
				deletedList.append(os.path.join(root, fileName))

# Display file number		
print str(count) + ' files deleted'

# Write to log file
if logFiles and len(deletedList) > 0:
	with open('Deleted files.txt', 'a') as log_file:
		log_file.write('The following files were deleted on %s \n\n' % time.strftime("%c"))
		for item in deletedList:
  			 log_file.write("%s \n" % item)