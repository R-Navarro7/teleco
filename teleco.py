import RPi.GPIO as GPIO                   
import time                                
relee = 17                         
GPIO.setmode(GPIO.BOARD)                  
GPIO.setup(relee, GPIO.OUT) 
GPIO.cleanup()

while True:                              
    GPIO.output(relee, True)      
    time.sleep(1)   
    GPIO.output(relee, False)   
    time.sleep(1)                   