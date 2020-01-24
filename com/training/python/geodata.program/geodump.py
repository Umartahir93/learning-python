import json
import codecs
import sqlite3


fhand = codecs.open('where.js', 'w', "utf-8") #why did here utf-8 was given
fhand.write("myData = [\n")
count = 0

conn = sqlite3.connect('geodata.sqlite')
spidercursor = conn.cursor()
spidercursor.execute('SELECT * FROM Locations')

for row in spidercursor:

    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")

    try:
        print(where, lat, lng)
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)

    except:
        continue

fhand.write("\n];\n")
spidercursor.close()
fhand.close()
