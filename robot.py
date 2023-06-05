# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
import socket
import RPi.GPIO as GPIO          
from time import sleep

ena = 18
enb = 16
in1 = 23
in2 = 24
in3 = 25
in4 = 12
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

ena=GPIO.PWM(ena,1000)
enb=GPIO.PWM(enb,1000)
ena.start(18)
enb.start(16)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

def forward():
    print("forward")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def backward():
    print("backward")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def left():
    print("left")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def right():
    print("right")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def stop():
    print("stop")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def low():
    print("low")
    ena.ChangeDutyCycle(25)
    enb.ChangeDutyCycle(25)

def medium():
    print("medium")
    ena.ChangeDutyCycle(50)
    enb.ChangeDutyCycle(50)

def high():
    print("high")
    ena.ChangeDutyCycle(75)
    enb.ChangeDutyCycle(75)

import socket

def move(command):
    if command == "forward":
        forward()
        # Add code here for moving forward
    elif command == "backward":
        backward()
        # Add code here for moving backward
    elif command == "left":
        left()
        # Add code here for moving left
    elif command == "right":
        right()
        # Add code here for moving right
    elif command == "stop":
        stop()
        # Add code here for stopping
    else:
        print("Invalid command")

def start_client():
    server_address = ('192.168.45.1', 8000)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    print("Connected to the server.")

    while True:
        try:
            command = client_socket.recv(1024).decode()
            move(command)
        except:
            print("Error receiving data. Closing connection.")
            break

    client_socket.close()

start_client()
