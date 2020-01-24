import  sqlite3, json, time
import ssl
import urllib.request, urllib.parse,urllib.error


serviceurl= "http://py4e-data.dr-chuck.net/geojson?"

conn = sqlite3.connect('geodata.sqlite')
spidercursor = conn.cursor()

spidercursor.execute('''
            Create TABLE IF NOT EXISTS Locations (address varchar(250), geodata varchar(250));''')

#BECAUSE PYTHON DOESNT COME WITH LEGIMATE CERTIFICATE SO
#ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


fileHandle = open("queue.data")
count = 0
for line in fileHandle:
    if count > 200:
        print('Retrieved 200 locations ! Restart to retrieve more')
        break

    address = line.strip()
    print(' ')

    spidercursor.execute("SELECT geodata FROM Locations WHERE address= ?",
                (memoryview(address.encode()),))

    try:
        data = spidercursor.fetchone([0])
        print("Found in database ",address)
        continue
    except:
        pass


    params = dict()
    params["query"] = address
    url = serviceurl+urllib.parse.urlencode(params)

    print("Retrieving",url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print('Retrived',len(data),'characters')
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print("FAILED TO RETRIEVE")
        print(data)
        break

    spidercursor.execute('''INSERT INTO Locations (address, geodata)
                VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit...')
        print(count)
        time.sleep(2)

spidercursor.close()





