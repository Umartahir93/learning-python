from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

def writeFileIntoDisk(fileName,content):
    file = open(fileName, "w")
    file.write(content)
    file.close()




#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    url = input("Enter Url - ")
    html = urllib.request.urlopen(url,context=ctx).read()
except:
    print("The url which you entered is broken or not reachable")
    exit()

htmlSoupProxy = BeautifulSoup(html,'html.parser')
writeFileIntoDisk("wholeWebSite.html",str(htmlSoupProxy))


anchorTags = htmlSoupProxy('a')
filename = ["HyperLinkfile%02d.html"%x for x in range(0,len(anchorTags))]

for index in range(0,len(anchorTags)):
    tag = anchorTags[index].get('href', [])
    if 'http' in tag:
        writeFileIntoDisk(filename[index],tag)




