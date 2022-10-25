import RPi.GPIO as GPIO
import board
import adafruit_dht
import psutil
import time

pins = [11,16,2] # relay, sensor_1, sensor_2

#def setup(pins):
    
    #setup_pin(pins[0], 0)
    #setup_pin(pins[1], 1)
    #setup_pin([pins[2]], 1)

def setup_pin(pin,mode_input):
    gpio_modes = GPIO.OUT, GPIO.IN
    mode = gpio_modes[mode_input]
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (pin,mode)

#setup(pins)

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

sensor = adafruit_dht.DHT11(board.D23)

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)

# for i in range(10):
#     GPIO.output(pins[0],True)
#     time.sleep(2)
#     GPIO.output(pins[0],False)
#     time.sleep(2)                 