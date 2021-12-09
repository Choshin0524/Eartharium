import RPi.GPIO as GPIO
import time
from sensor_module import DHT22

def get_DHTsensor_info():
    DHTPin = 11
    #クラス初期化
    dht = DHT22.DHT(DHTPin) 
    #動作確認
    for i in range(20):
        chk = dht.readDHT22()
        if chk is dht.DHTLIB_OK:
            print("check OK!")
            break
        time.sleep(0.1)

    #計測結果文字列に変換しを配列に格納
    humidity, temperature = str(dht.humidity),str(dht.temperature)
    if len(humidity) == 1:
        humidity = " " + humidity
    if len(temperature) == 1:
        temperature = " " + temperature
    result = [humidity,temperature]
    
    return result