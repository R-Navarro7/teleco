import RPi.GPIO as GPIO
import Adafruit_DHT
import time

pins = [11,7,2] # relay, sensor_1, sensor_2

def setup(pins):
    
    #setup_pin(pins[0], 0)
    setup_pin(pins[1], 1)
    #setup_pin([pins[2]], 1)

def setup_pin(pin,mode_input):
    gpio_modes = GPIO.OUT, GPIO.IN
    mode = gpio_modes[mode_input]
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (pin,mode)

setup(pins)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    time.sleep(0.5)

# for i in range(10):
#     GPIO.output(pins[0],True)
#     time.sleep(2)
#     GPIO.output(pins[0],False)
#     time.sleep(2)                 