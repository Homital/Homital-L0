#import wifimgr
import network
from time import sleep
import machine
try:
    import ujson as json
except:
    import json
import np

'''
try:
  import usocket as socket
except:
  import socket
'''

#wlan = wifimgr.get_connection()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("connecting to wifi...")
    try:
        f = open('wifi.json')
        wifi = json.load(f)
        f.close()
        wlan.connect(wifi['ssid'], wifi['password'])
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())
    except:
        print("Please upload a valid wifi.json file to the board first")
        while True:
            np.showerror()

# Main Code goes here
print("Homital L0 OK~")

np.startup()

np.main()