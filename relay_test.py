import RPi.GPIO as GPIO
import time

relay_pin = 37

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relay_pin,GPIO.OUT)
    GPIO.output(relay_pin.GPIO.LOW)

def loop():
    while True:
        GPIO.output(relay_pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relay_pin,GPIO.LOW)
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()