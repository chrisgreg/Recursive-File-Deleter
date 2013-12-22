Recursive-File-Deleter
======================

A Python script to recursively run through folders and delete files based on file name and extension

Example use:

python Recursive\ File\ Deleter.py "/Users/defaultUser/Downloads/" ".mp3" log

The above line would cause the script to go to the Downloads folder of the default user, and proceed to recursively delete every mp3 file in that folder and all sub-folders. A log would be produced in the domain the script was called from containing the paths of the files deleted and the date/time the script was used.
