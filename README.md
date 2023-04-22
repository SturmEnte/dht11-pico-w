# dht11-pico-w

## About
This is a micropython script for the Raspberry Pi Pico W in use with a DHT11 sensor. If you send a http request to the Raspberry Pi Pico will you receive the current temperature and humidity read by the sensor.

## How to use
1. Upload the DHT11 micropython library to the Pico
2. Upload a Python file called "secrets.py" with a variable called "SSID" containing the wifi's ssid and a variable called "PASSWORD" containing the wifi's password
3. Upload main.py from this repository to the Pico

## Wifi connection
If the Pico is not connected to the wifi will the onboard led be activated. If it disconnects from the wifi will it try to reconnect to the wifi until it reconnects
