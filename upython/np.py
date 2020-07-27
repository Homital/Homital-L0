from machine import Pin
from neopixel import NeoPixel
import homital
import time
try:
    import ujson as json
except:
    import json

num = 8
np = NeoPixel(Pin(0, Pin.OUT), num)

def startup():
    for i in range(num):
        np[i] = (255, 0, 0)
        np.write()
        time.sleep_ms(125)
    for i in range(num):
        np[i] = (0, 255, 0)
        np.write()
        time.sleep_ms(125)
    for i in range(num):
        np[i] = (0, 0, 255)
        np.write()
        time.sleep_ms(125)
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()

def showerror():
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()
    for i in range(num):
        np[i] = (255, 0, 0)
        np.write()
        time.sleep_ms(125)

def connecting():
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()
    for i in range(num):
        for j in range(num):
            np[j] = (255, 0, 0) if j == i else (0, 0, 0)
        np.write()
        time.sleep_ms(500)

def default_mode(update_interval_ms):
    print("Running np.default_mode(%d)" % (update_interval_ms,))
    colormode = 0
    while True:
        try:
            st = homital.getStatus()
            print('status: %s' % (str(st),))
            if st['success']:
                st = st['status']
                power = st['power']
                color = (0,255,0) if colormode==0 else (0,0,255) if colormode==1 else (0,255,255) if colormode==2 else (50,50,50)
                color = color if power else (20, 20, 20)
                colormode = 0 if colormode==2 else colormode+1
                for i in range(num):
                    np[i] = color
                np.write()
            else:
                print('getting status failed')
        except:
            print("unknown error when getting status")
        time.sleep_ms(update_interval_ms)

def main():
    print('Running np.main()')
    print('Testing connection to Homital-Core...')
    connecting()
    if (not homital.isConnected()):
        print('Connection Failed!')
        while True:
            showerror()
    print('Connected!')
    try:
        import modes
    except:
        default_mode(1000)