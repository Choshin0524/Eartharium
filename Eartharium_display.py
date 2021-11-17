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

#LCDディスプレイのセットアップ
if __name__ == "__main__":
    PCF8574_address = 0x27
    mcp = PCF8574_GPIO(PCF8574_address)
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
    mcp.output(3,1)
    lcd.begin(16,2)
    lcd.cursor(3,0)
    lcd.message("Welcome to")
    lcd.cursor(3,1)
    lcd.message("Earthrium")
    time.sleep(2)
    lcd.clear()

def get_weather_list():
    global weather_list
    weather_list = get_weather.get_weather_info() #weather_list[0]:high temp [1]:low temp [2]:weather

def get_time():
    global time_now
    time_now = datetime.datetime.now().strftime("%H:%M")    

def show_time():
    lcd.cursor(0,0)
    lcd.message(time_now)

def show_weather():
    lcd.cursor(8,0)
    lcd.message(weather_list[2])
    lcd.cursor(0,1)
    lcd.message(str(weather_list[0])+"  "+str(weather_list[1]))

#定時実行のスケジューリング
schedule.every(1).seconds.do(get_time)
schedule.every(2).minutes.do(get_weather_list)

while True:
    schedule.run_pending()
    show_time()
    show_weather()
    time.sleep(1)
    lcd.clear()
    
    
    
    

    

    

    

    