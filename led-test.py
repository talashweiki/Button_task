import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print(GPIO.input(3))
    if GPIO.input(3) == GPIO.LOW:
        print("Button was pushed!")
        print("LED on!")
        GPIO.output(2,GPIO.HIGH)
    if GPIO.input(3) == GPIO.HIGH:
        print("led is off!")
        GPIO.output(2,GPIO.LOW)
  
