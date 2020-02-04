import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

# blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel, we set GPIO4 (Pin 7) to OUTPUT
GPIO.setup(7, GPIO.OUT)
#GPIO.setup(11, GPIO.OUT)

# blink GPIO4 (Pin 7) 50 times
for i in range(0,10):
    #blink(11)
    blink(7)

GPIO.cleanup()
