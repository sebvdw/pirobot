import time
value = 0
increment = 1

while True:
    print("Current value:", value)

    value += increment
    time.sleep(0.01)
    if value == 180 or value == 0:
        increment *= -1
