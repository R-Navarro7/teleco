import RPi.GPIO as GPIO
import time

def setup():
    relee, sensor_1, sensor_2 = 11,1,2
    setup_pin(relee, 0)
    setup_pin(sensor_1, 1)
    setup_pin(sensor_2, 1)

def setup_pin(pin,mod):
    modes = GPIO.OUT, GPIO.IN
    mode = modes[mod]
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (pin,mode)



for i in range(10):
    GPIO.output(8,True)
    time.sleep(2)
    GPIO.output(8,False)
    time.sleep(2)                 