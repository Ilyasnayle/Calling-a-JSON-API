import urllib.parse
import urllib.request
import json
import ssl  # Importing the ssl module for ignoring SSL certificate errors

serviceurl = "https://py4e-data.dr-chuck.net/opengeo?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")

    if len(address) < 1: 
        break
    
    address = address.strip()
    parms = {'q': address}

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    try:
        # Open the URL with SSL context
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode('utf-8')
        print('Retrieved', len(data), 'characters')
        
        js = json.loads(data)

        if 'features' not in js:
            print('==== No Results Found ====')
            continue

        place_id = js['features'][0]['properties']['plus_code']
        print("Place id", place_id)
        
    except Exception as e:
        print('==== Failure To Retrieve ====')
        print(e)
