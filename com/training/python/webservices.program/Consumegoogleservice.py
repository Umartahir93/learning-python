import json
import urllib.parse, urllib.request, urllib.error


serviceUrl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    location = input("Enter the location ")
    if len(location) < 1 : break
    url = serviceUrl + urllib.parse.urlencode({'address':location})
    print("Retreiving from url" , url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    print("Reterieved data length ", len(data))

    try:
        js = json.loads(data)
    except:
        js = None


    if not js or 'status' not in js or js['status'] != 'OK':
        print("Failed to retrieve data ")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    #parse json to get data
    #its simple
    #since I do not have its key I am not able to parse it
    #way of getting data is same as before




