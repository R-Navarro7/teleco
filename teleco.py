import RPi.GPIO as GPIO
import board
import adafruit_dht
import psutil
import time

out_pin = 17 # relay, sensor_1, sensor_2
temp_threshold = 25
humidity_theshold = 50

actuator_on = False

def setup(pin):   
    mode = GPIO.OUT
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (pin,mode)

setup(out_pin)

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

sensor = adafruit_dht.DHT11(board.D23)

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print(f"Temperature: {temp}*C   Humidity: {humidity}% ")
        if (temp > temp_threshold and humidity > humidity_theshold) and actuator_on:
            GPIO.output(out_pin, GPIO.HIGH)
        if (temp > temp_threshold and humidity > humidity_theshold) and not actuator_on:
            GPIO.output(out_pin, GPIO.LOW)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)

             