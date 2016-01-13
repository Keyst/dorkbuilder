import time
##The script asks you to give dork parameters: intext, inurl, ext, ... 
##Users interact with a simple command line input
yes = "y" or "yes" or "Y"   #define yes response
#####################################################################################
#####################################################################################
#####################################################################################
intextyn = raw_input("Search for a specific text in the page? Y/N : ")
if intextyn==yes:
            intext = raw_input("In the page I am searching is wrote this: ")
else:
            intext = None
#####################################################################################
inurlyn = raw_input("Search for a specific URL? Y/N : ")
if inurlyn==yes:
            inurl = raw_input("I want to search only for this URL: ")
else:
            inurl = None
#####################################################################################
extyn = raw_input("Search for a specific file extension? Y/N : ")
if extyn==yes:
            ext = raw_input("I want to search for files with this extension: ")
else:
            ext = None
#####################################################################################
linkyn = raw_input("Searching for links in webpages? Y/N : ")
if linkyn==yes:
            link = raw_input("Search for this link in webpages: ")
else:
            link = None
#####################################################################################
intitleyn = raw_input("Looking for words in titles and pages? Y/N : ")
if intitleyn==yes:
            intitle = raw_input("Enter the word in title and in page: ")
else:
            intitle = None
####################################################################################

print "Processing..."
time.sleep(1)

#Defining variables to delete in case of null

inurlout = "inurl:"
intextout = "intext:"
linkout = "link:"
extout = "ext:"
intitleout = "intitle:"

if inurl==None:
       inurlout = ""
       inurl = ""
if intext==None:
       intextout = ""
       intext = ""
if link==None:
       linkout = ""
       link = ""
if ext==None:
       extout = ""
       ext = ""
if intitle==None:
       intitleout = ""
       intitle = ""

print(inurlout+inurl+" "+intextout+intext+" "+linkout+link+" "+extout+ext+" "+intitleout+intitle)
