import re

inputstring = 'THe numbers in my string are 12 and 13 and 14'
y = re.findall('[0-9]+',inputstring)
print(y)

inputstring = 'From: my email is umar.tahir@northbaysolutions'
y = re.findall('\S+@\S+',inputstring)

print(y)

y = re.findall('@(\S+)',inputstring)
print(y)

#SPAM CHECKER
filehandler = open('spam-checker.txt')
maximum = list()
for line in filehandler:
    line = line.strip()
    stuff = re.findall('^X-DSPAM-CONFIDENCE: ([0-9]+)',line)
    if len(stuff) != 1 : continue
    num = int(stuff[0])
    maximum.append(num)

print('Maximum number is',max(maximum))


