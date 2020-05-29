from machine import Pin
from neopixel import NeoPixel
import time
try:
    import ujson as json
except:
    import json

num = 8
np = NeoPixel(Pin(0, Pin.OUT), num)

def startup():
    print("Running np.startup()")
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()
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
    print("Running np.showerror()")
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()
    for i in range(num):
        np[i] = (255, 0, 0)
        np.write()
        time.sleep_ms(125)
    for i in range(num):
        np[i] = (0, 0, 0)
        np.write()
        time.sleep_ms(125)

def default_mode(update_interval_ms):
    print("Running np.default_mode(%d)" % (update_interval_ms,))
    first_time = True
    import homitalcore
    while True:
        try:
            st = homitalcore.getStatus()
            if st['success']:
                if first_time:
                    first_time = False
                    power = st['power']
                    color = (0, 255, 0) if power else (30, 30, 30)
                    for i in range(num):
                        np[i] = color
                    np.write()
                elif st['power'] != power:
                    power = not power
                    color = (0, 255, 0) if power else (30, 30, 30)
                    for i in range(num):
                        np[i] = color
                    np.write()
            else:
                print('getting status failed')
        except:
            print("unknown error when getting status")
        time.sleep_ms(update_interval_ms)

def main():
    print("Running np.main()")
    import homitalcore
    print("Testing connection to server...")
    while(not homitalcore.isConnected()):
        pass
    print("Connected!")
    homitalcore.checkForUpdate()
    try:
        import modes
    except:
        default_mode(100)