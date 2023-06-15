import socket
import RPi.GPIO as GPIO          
from time import sleep
from ultrasonicsensor import ultrasonicRead
import sys
import time
from target import *

#Ultrasonic Sensor
TRIG = 20
ECHO = 21

#Servo
servoPin = 26

# setup the servo and ultrasonic
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 50)
servo.start(7)
print("Starting radar")
# targets list
targets = {}

try:
    while True:

        # rotate from 0 to 180
        for angle in range(0, 180):
            
            distance = ultrasonicRead(GPIO, TRIG, ECHO)
            
            # change the condition if the range is changed
            if distance != -1 and distance <= 50:
                targets[angle] = Target(angle, distance)

            angle = 180 - angle
            dc = 1.0 / 18.0 * angle + 2
            servo.ChangeDutyCycle(dc)

            print(distance)

            time.sleep(0.001)
            

        # rotate from 180 to 0
        for angle in range(180, 0, -1):
            
            distance = ultrasonicRead(GPIO, TRIG, ECHO)
            
            # change the condition if the range is changed
            if distance != -1 and distance <= 50:
                targets[angle] = Target(angle, distance)

            angle = 180 - angle
            dc = 1.0 / 18.0 * angle + 2
            servo.ChangeDutyCycle(dc)

            print(distance)

            time.sleep(0.001)
            

            
except KeyboardInterrupt:
    print('Radar Exit')
    servo.stop()
    GPIO.cleanup()
    
except Exception as e:
    print(e)
    print('Radar Exit')
    servo.stop()
    GPIO.cleanup()
    
    
sys.exit()
