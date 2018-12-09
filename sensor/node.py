import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.IN)


while True:
    input=GPIO.input(17)
    if input==1:
        print("Intruder Detected")
        os.system('raspistill -o /home/pi/Documents/intruder.jpg')
        print("capture successful")
        print ("LED on")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(2)
        print ("LED off")
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
    else:
        print("No Intruder")
        time.sleep(1)
