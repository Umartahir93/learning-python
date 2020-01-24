import xml.etree.cElementTree as ET
import json
data ='''
    <person>
        <name> Umar Tahir </name>
        <cellnumber> 0303 4807079 </cellnumber>
        <address> Lahore </address>
    </person>
'''

tree = ET.fromstring(data)
print("Name ", tree.find('name').text)

#in order to get list of tags user findAll

jsondata = '''
[
    {
        "id": "1",
        "name" : "Umar Tahir"
        
    },
    {
        
        "id": "1",
        "name" : "Umar Tahir"
    
    }

]
'''

info = json.loads(jsondata)
print(info[0]["id"])

