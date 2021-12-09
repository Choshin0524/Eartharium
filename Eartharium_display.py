# このファイルは__main__ファイルとして実行される

from lcd_module.PCF8574 import PCF8574_GPIO
from lcd_module.Adafruit_LCD1602 import Adafruit_CharLCD
from weather_module import get_weather
import schedule
import time
import datetime
import Net_test
import DHTget

# 初期化
weather_list = []
time_now = ""

def get_DHTsensor_list():
    global DHTsensor_list
    try:
        #DHTsensor_list [0] room humidity [1] room temp
        DHTsensor_list = DHTget.get_DHTsensor_info()
    except:
        lcd.setCursor(0, 0)
        lcd.message("error")
            
def get_weather_list():
    global weather_list
    try:
        # weather_list[0]:temp_now [1]condition
        weather_list = get_weather.get_weather_info()
    except:
        lcd.setCursor(0, 0)
        lcd.message("error")
    #刷新
    lcd.setCursor(1, 1)
    lcd.message(" "*15)

def get_time():
    global time_now
    time_now = datetime.datetime.now().strftime("%H:%M")

def show_DHTsensor_value():
    lcd.setCursor(0,0)
    lcd.message("Room Humidity:" + DHTsensor_list[0])
    lcd.setCursor(0,1)
    lcd.message("Room Temp:" + DHTsensor_list[1])

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
        lcd.setCursor(0, 1)
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
schedule.every(1).minutes.do(get_DHTsensor_list)
schedule.every(2).minutes.do(get_weather_list)

def loop():
    while True:
        schedule.run_pending()
        #時間と天気情報表示
        show_time()
        show_weather()
        time.sleep(2)
        lcd.clear()
        #センサー情報表示
        show_DHTsensor_value()
        time.sleep(2)
        lcd.clear()
        
if __name__ == "__main__":
    print('Earthrium is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()