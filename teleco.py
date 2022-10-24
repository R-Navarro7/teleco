import RPi.GPIO as GPIO                   
import time                                
GPIO.cleanup()
relee = 17                         
GPIO.setmode(GPIO.BCM)                  
GPIO.setup(relee, GPIO.OUT) 

while True:                              
    GPIO.output(relee, True)      
    time.sleep(1)   
    GPIO.output(relee, False)   
    time.sleep(1)                   