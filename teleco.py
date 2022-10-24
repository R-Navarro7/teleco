import RPi.GPIO as GPIO                   
import time                                

relee = 11                           
GPIO.setmode(GPIO.BCM)                  
GPIO.setup(relee, GPIO.OUT) 

while True:                              
    GPIO.output(relee, GPIO.HIGH)      
    time.sleep(1)   
    GPIO.output(relee, GPIO.LOW)   
    time.sleep(1)                   