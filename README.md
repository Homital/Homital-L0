# Homital-L0
The zeroth light of the homital family

## Setup

- Upload the latest micropython firmware to the ESP8266 board (refer to [this page](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro))
- Upload all the `.py` files from this repository to the ESP8266 board (possibly through [Thonny IDE](https://thonny.org/))
- Create a `wifi.json` file with the following structure (possibly through [Thonny IDE](https://thonny.org/)):

```json
{
  "ssid": "<YOUR-SSID>",
  "password": "YOUR-PASSWORD"
}
```

- Create a `credentials.json` file with the following structure (possibly through [Thonny IDE](https://thonny.org/)):

```json
{
  "id": "<DEVICE-ID>",
  "token": "<BEARER-TOKEN-FOR-AUTHORIZATION>",
  "version": "<SOFTWARE-VERSION>",
  "SERVER_ADDR": "<ROOT-ENDPOINT>"
}
```

- Restart the device and hook up a UART cable to see the debug messages and test the device
