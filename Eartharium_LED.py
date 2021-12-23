import RPi.GPIO as GPIO
import datetime
import time
import sys

LEDpin = 40
set_hour = ([6,10],[11,15],[16,19],[20,23],[0,5])
time_now_hour = 0
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDpin,GPIO.OUT)
    GPIO.output(LEDpin,GPIO.LOW)

def LEDon(duty):
        GPIO.output(LEDpin,GPIO.HIGH)
        time.sleep(0.1*duty)
        GPIO.output(LEDpin,GPIO.LOW)
        time.sleep(0.1*(1-duty))
        
def loop():
    time_now_hour = datetime.datetime.now().hour
    for i in range (0,5):
        if time_now_hour >= set_hour[i][0] and time_now_hour <= set_hour[i][1]:
            if i == 0:
                duty = 0.5
            if i == 1:
                duty = 1.0
            if i == 2:
                duty = 0.4
            if i == 3 or i == 4:
                duty = 0.1
    LEDon(duty)

setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.output(LEDpin,GPIO.LOW)
        sys.exit()