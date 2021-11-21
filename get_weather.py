from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import time
import sys

def get_weather_info():
    option = Options()                          # オプションを用意
    option.add_argument('--headless')
    CHROME_DRIVER = '/usr/lib/chromium-browser/chromedriver'
    browser = webdriver.Chrome(CHROME_DRIVER,options=option)

    #Weather.com
    url_id = "https://weather.com/weather/today/l/647e251db6b21b336371be6d2ed34197f13ea10334f06c720fed781c27c9c832"
    browser.get(url_id)
    time.sleep(5)

    #天気情報取得
    tempele_now = browser.find_element_by_class_name("CurrentConditions--tempValue--3a50n")
    conditonele_now = browser.find_element_by_class_name("CurrentConditions--phraseValue--2Z18W")

    #°記号を取り除く
    num_regex = re.compile(r'\d+')
    temp_deg_removed = num_regex.search(tempele_now.text)

    #摂氏変換
    tempele_now_value = str(int(round((int(temp_deg_removed.group())-32)/1.8,0)))
    
    #温度が１桁の場合，温度のまえにスペース２つを加える．
    if len(tempele_now_value) == 1:
        tempele_now_value = " 　" + tempele_now_value
    
    #温度が２桁の場合，温度のまえにスペース１つを加える．
    if len(tempele_now_value) == 2:
        tempele_now_value = " " + tempele_now_value
    
    weather_info_array = [tempele_now_value,conditonele_now.text]

    #終了
    print("天気情報取得OK.")
    return weather_info_array