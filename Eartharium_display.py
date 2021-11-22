# このファイルは__main__ファイルとして実行される

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import get_weather
import schedule
import time
import datetime
import Net_test

# 初期化
weather_list = []
time_now = ""

def get_weather_list():
    global weather_list
    try:
        # weather_list[0]:temp_now [1]condition
        weather_list = get_weather.get_weather_info()
    except:
        lcd.setCursor(0, 0)
        lcd.message("error")
    lcd.setCursor(1, 1)
    lcd.message(" "*15)

def get_time():
    global time_now
    time_now = datetime.datetime.now().strftime("%H:%M")

def show_time():
    lcd.setCursor(0, 0)
    lcd.message(time_now)

def show_weather():
    lcd.setCursor(6, 0)
    lcd.message("TEMP:"+weather_list[0]+"'C")
    lcd.setCursor(0, 1)
    #表示しきれないときはシフト
    if len(weather_list) == 2:
        lcd.message(weather_list[1])
    if len(weather_list) == 3:
        lcd.message(weather_list[1])
        time.sleep(2)
        lcd.message(" "*16) #下の列だけクリア
        lcd.message(weather_list[2])
        time.sleep(2)

def destroy():
    lcd.clear()

# LCDディスプレイのセットアップ
if __name__ == "__main__":
    PCF8574_address = 0x27
    mcp = PCF8574_GPIO(PCF8574_address)
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)
    mcp.output(3, 1)
    lcd.begin(16, 2)
    #Welcome to Earthrium 表示
    lcd.setCursor(3, 0)
    lcd.message("Welcome to")
    lcd.setCursor(3, 1)
    lcd.message("Earthrium")
    time.sleep(2)
    lcd.clear()
    #ネットワーク接続中　表示
    lcd.setCursor(0,0)
    lcd.message("Connecting to")
    lcd.setCursor(0,1)
    lcd.message("the internet...")
    #ネット接続を確認してから進む
    Net_test.network_test()
    lcd.clear()
    lcd.setCursor(4, 0)
    lcd.message("Loading")
    lcd.setCursor(4, 1)
    lcd.message("Weather")
    get_weather_list()
    lcd.clear()

# 定時実行のスケジューリング
schedule.every(1).seconds.do(get_time)
schedule.every(2).minutes.do(get_weather_list)

def loop():
    while True:
        schedule.run_pending()
        show_time()
        show_weather()

if __name__ == "__main__":
    print('Earthrium is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()