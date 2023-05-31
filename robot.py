import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        GPIO.output(24, GPIO.HIGH)  # Set pin 25 to high (3.3V)
        
        # Wait for some time
        # You can add your code here or use time.sleep() for a delay
        
        GPIO.output(24, GPIO.LOW)  # Set pin 25 to low (0V)
        
        # Wait for some time
        # You can add your code here or use time.sleep() for a delay

except KeyboardInterrupt:
    print("Terminating the script.")
    GPIO.cleanup()
