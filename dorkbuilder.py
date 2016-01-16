import time
##The script asks you to give dork parameters: intext, inurl, ext, ... 
##Users interact with a simple command line input
yes = "y" or "yes" or "Y"   #define yes response
#####################################################################################
#####################################################################################
#####################################################################################
intextyn = raw_input("Search for a specific text in webpages? Y/N : ")
if intextyn==yes:
            intext = raw_input("In the page I am searching is written this: ")
else:
            intext = None
#####################################################################################
inurlyn = raw_input("Search for specific words in URLs? Y/N : ")
if inurlyn==yes:
            inurl = raw_input("I want to search only for this URLs: ")
else:
            inurl = None
#####################################################################################
siteyn = raw_input("Search only for a specific website? Y/N: ")
if siteyn==yes
            site = raw_input("Insert the URL of the website: ")
else:
            site = None
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
siteout = "site:"

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
if site==None:
       siteout = ""
       site = ""
       
dork = (siteout+site+" "+inurlout+inurl+" "+intextout+intext+" "+linkout+link+" "+extout+ext+" "+intitleout+intitle)
print(dork)
######################################################################################################
######################################################################################################

#Now splinter will search the dork for you...
searchyn = raw_input("Do you want to search the dork now? Y/N: ")
if searchyn=="y":
     print "Opening browser and searching your dork for you..."

     from splinter import Browser

     with Browser() as firefox:
       firefox.visit("http://www.google.com")
       firefox.reload()
       firefox.visit("http://www.google.com")
       time.sleep(1)
       firefox.fill('q', dork)
       button = firefox.find_by_name('btnK')
       button.click()
       time.sleep(100000000)
else:
     print "Enjoy your dork :)"    
