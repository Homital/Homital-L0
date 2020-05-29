try:
    import json
except:
    import ujson as json

try:
    f = open('credentials.json')
    credentials = json.load(f)
    f.close()
except:
    print('something went wrong when loading credentials')
    import np
    while True:
        np.showerror()

SERVER_ADDR = credentials['SERVER_ADDR']

import urequests as requests

def isConnected():
    try:
        res = requests.get(SERVER_ADDR + '/device', headers={'Authorization':'Bearer ' + credentials['token']})
        rj = res.json()
        res.close()
        return rj['success']
    except:
        return False

def getStatus():
    try:
        res = requests.get(SERVER_ADDR + '/device/status', headers={'Authorization':'Bearer ' + credentials['token']})
        rj = res.json()
        res.close()
        st = rj['status']
        st['success'] = True
        return st
    except:
        return {'success': False}

def checkForUpdate():
    print("Currently running Homital-L0 %s" % (credentials['version']))
    print("Searching for updates...")
    try:
        res = requests.get(SERVER_ADDR + '/device/updates/homital-l0', headers={'Authorization':'Bearer ' + credentials['token']})
        rj = res.json()
        res.close()
        if rj['success'] == True:
            print('Versions available:')
            rj['versions'].sort() #only work for single number versions
            for v in rj['versions']:
                print("  %s" % (v,))
            if rj['versions'][-1] > credentials['version']:
                print("New version available: %s" % (rj['versions'][-1],))
                print("But sadly I cannot automatically install the update yet :<")
                print("You can try installing the update yourself")
                print("See %s" % ("https://github.com/Homital/Homital-L0"))
            else:
                print("Already running the latest version!")
    except:
        print("Something went wrong when checking for updates, skipping...")
#Download the update and replace the existing script... (better keep a backup)
#Update version number in credentials.json
def fetchUpdate(version):
    print("Updating to %s..." % (version))