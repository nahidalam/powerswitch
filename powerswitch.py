import time
import RPi.GPIO as io
io.setmode(io.BCM)

power_pin = 23

io.setup(power_pin, io.OUT)
io.output(power_pin, False)

while True:
    nb = raw_input('Choose a number: ')
    try:
     number = int(nb)
    except ValueError:
     print("Invalid number")
    if number>0:
        print("POWER ON")
        io.output(power_pin, True)
        time.sleep(5);
    else:
        print("POWER OFF")
        io.output(power_pin, False)
        time.sleep(5)
    time.sleep(1)
