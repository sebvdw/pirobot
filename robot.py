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


# Define the server's IP address and port
server_ip = '192.168.45.1'  # Replace with the server's IP address
server_port = 8000  # Replace with the server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Main loop to receive instructions from the server
while True:
    # Receive data from the server
    data = client_socket.recv(1024).decode()

    # Check the received instruction and execute the corresponding function
    if data == 'forward':
        forward()
    elif data == 'backward':
        backward()
    elif data == 'left':
        left()
    elif data == 'right':
        right()
    else:
        print("Invalid command")

# Close the socket connection
client_socket.close()

# while(1):
#     x=input()
#     if x=='s':
#         print("stop")
#         GPIO.output(in1,GPIO.LOW)
#         GPIO.output(in2,GPIO.LOW)
#         GPIO.output(in3,GPIO.LOW)
#         GPIO.output(in4,GPIO.LOW)
#         x='z'

#     elif x=='f':
#         print("forward")
#         GPIO.output(in1,GPIO.HIGH)
#         GPIO.output(in2,GPIO.LOW)
#         GPIO.output(in3,GPIO.HIGH)
#         GPIO.output(in4,GPIO.LOW)
#         x='z'

#     elif x=='b':
#         print("backward")
#         GPIO.output(in1,GPIO.LOW)
#         GPIO.output(in2,GPIO.HIGH)
#         GPIO.output(in3,GPIO.LOW)
#         GPIO.output(in4,GPIO.HIGH)
#         x='z'

#     elif x=='l':
#         print("left")
#         GPIO.output(in1,GPIO.LOW)
#         GPIO.output(in2,GPIO.HIGH)
#         GPIO.output(in3,GPIO.HIGH)
#         GPIO.output(in4,GPIO.LOW)
#         x='z'
    
#     elif x=='r':
#         print("right")
#         GPIO.output(in1,GPIO.HIGH)
#         GPIO.output(in2,GPIO.LOW)
#         GPIO.output(in3,GPIO.LOW)
#         GPIO.output(in4,GPIO.HIGH)
#         x='z'

#     elif x=='b':
#         print("backward")
#         GPIO.output(in1,GPIO.LOW)
#         GPIO.output(in2,GPIO.HIGH)
#         GPIO.output(in3,GPIO.LOW)
#         GPIO.output(in4,GPIO.HIGH)
#         x='z'

#     elif x=='sl':
#         print("low")
#         ena.ChangeDutyCycle(25)
#         enb.ChangeDutyCycle(25)
#         x='z'

#     elif x=='sm':
#         print("medium")
#         ena.ChangeDutyCycle(50)
#         enb.ChangeDutyCycle(50)
#         x='z'

#     elif x=='sh':
#         print("high")
#         ena.ChangeDutyCycle(75)
#         enb.ChangeDutyCycle(75)
#         x='z'
    
#     elif x=='e':
#         GPIO.cleanup()
#         print("GPIO Clean up")
#         break
    
#     else:
#         print("<<<  wrong data  >>>")
#         print("please enter the defined data to continue.....")