import RPi.GPIO as GPIO
import time

pins = [11,1,2] # relay, sensor_1, sensor_2

def setup(pins):
    
    setup_pin(pins[0], 0)
    #setup_pin(pins[1], 1)
    #setup_pin([pins[2]], 1)

def setup_pin(pin,mode_input):
    gpio_modes = GPIO.OUT, GPIO.IN
    mode = gpio_modes[mode_input]
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (pin,mode)

setup(pins)

for i in range(10):
    GPIO.output(8,True)
    time.sleep(2)
    GPIO.output(8,False)
    time.sleep(2)                 