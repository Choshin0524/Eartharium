#このファイルは__main__ファイルとして実行される

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import get_weather
import schedule
import time
import datetime

#初期化
weather_list = []
time_now = ""

def get_weather_list():
    global weather_list
    try:
        weather_list = get_weather.get_weather_info() #weather_list[0]:high temp [1]:low temp [2]:weather
    except:
        lcd.setCursor(0,0)
        lcd.message("error")


def get_time():
    global time_now
    time_now = datetime.datetime.now().strftime("%H:%M:%S")   

def show_time():
    lcd.setCursor(0,0)
    lcd.message(time_now)

def show_weather():
    lcd.setCursor(9,0)
    lcd.message(weather_list[2])
    lcd.setCursor(0,1)
    lcd.message("High:"+str(weather_list[0])+"  Low:"+str(weather_list[1]))

def destroy():
    lcd.clear()

#LCDディスプレイのセットアップ
if __name__ == "__main__":
    PCF8574_address = 0x27
    mcp = PCF8574_GPIO(PCF8574_address)
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
    mcp.output(3,1)
    lcd.begin(16,2)
    lcd.setCursor(3,0)
    lcd.message("Welcome to")
    lcd.setCursor(3,1)
    lcd.message("Earthrium")
    time.sleep(2)
    lcd.clear()
    lcd.setCursor(4,0)
    lcd.message("Getting")
    lcd.setCursor(4,1)
    lcd.message("Weather")
    get_weather_list()
    lcd.clear()

#定時実行のスケジューリング
schedule.every(1).seconds.do(get_time)
schedule.every(2).minutes.do(get_weather_list)

def loop():
    while True:
        schedule.run_pending()
        show_time()
        show_weather()

if __name__ == "__main__":
    
    print ('Earthrium is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    
    

    

    

    

    