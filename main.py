from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum
import network
import secrets
import time
import socket
import json

# Meassure function
def meassure():
    try:
        return ((sensor.temperature), (sensor.humidity))
    except:
        return 

pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

# Connect wo wlan
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)
        
        m = meassure()
    
        if m:
            cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
            cl.send("{\"temperature\":%s, \"humidity\":%s}" % (m[0], m[1]))
        else:
            cl.send('HTTP/1.0 500 OK\r\nContent-type: application/json\r\n\r\n')
            cl.send("{\"error\":\"Error while reading sensor data\"}")
        
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')
