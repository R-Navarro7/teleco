import RPi.GPIO as GPIO
import board
import adafruit_dht
import psutil
import time
import subprocess
from get_ip import *

ip = "192.168.1.169"

out_pin = 17 # relay
temp_threshold = 15
humidity_theshold = 55

actuator_on = False

def setup(pin):   
    GPIO.cleanup()
    mode = GPIO.OUT
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (pin,mode, initial=GPIO.HIGH)

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
        if (temp > temp_threshold and humidity > humidity_theshold) and not actuator_on:
            GPIO.output(out_pin, GPIO.LOW)
            actuator_on = True
            print("actuador encendido")
        if (temp < temp_threshold or humidity < humidity_theshold) and actuator_on:
            GPIO.output(out_pin, GPIO.HIGH)
            actuator_on = False
            print("actuador apagado")

        bashCommand = f"/usr/bin/curl -d temp={temp} -d hum={humidity} -X POST http://{ip}:8000/iot/post/"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(5.0)

