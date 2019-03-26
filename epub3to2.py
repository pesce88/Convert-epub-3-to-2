import os, fnmatch

listOfFiles = os.listdir('.')  
pattern = "*.epub"  
for entry in listOfFiles:  
    if fnmatch.fnmatch(entry, pattern):
        os.rename(entry, entry+'zip')