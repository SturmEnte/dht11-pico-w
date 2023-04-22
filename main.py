from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

def meassure():
    try:
        return ((sensor.temperature), (sensor.humidity))
    except:
        return 

while True:
    m = meassure()
    
    if m:
        print("Temperature: {}".format(m[0]))
        print("Humidity: {}".format(m[1]))
    else:
        print("Failed to read sensor")
        
    time.sleep(1)
