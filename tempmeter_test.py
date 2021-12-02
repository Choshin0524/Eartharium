import RPi.GPIO as GPIO
import time
import DHT22

DHTPin = 11

def loop():
    dht = DHT22.DHT(DHTPin) #クラス初期化]
    while True:
        for i in range (20):
            chk = dht.readDHT22()
            if chk is dht.DHTLIB_OK:
                print("check OK!")
                break
            time.sleep(0.1)
        print("湿度は：{:.2}   温度は：{:.2}".format(dht.humidity,dht.temperature))
        time.sleep(2)

print("start...")
try:
    loop()
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
