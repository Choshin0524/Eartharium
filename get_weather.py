from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import re

def get_weather_info():
    CHROME_DRIVER = '/usr/lib/chromium-browser/chromedriver'
    browser = webdriver.Chrome(CHROME_DRIVER)
    
    #Yahoo Weather
    url_id = "https://weather.yahoo.co.jp/weather/jp/35/8120.html"
    browser.get(url_id)

    #天気情報取得
    tempele_today_high = browser.find_element_by_class_name("high")
    tempele_today_low = browser.find_element_by_class_name("low")
    weather_today = browser.find_element_by_class_name("pict")
    
    #天気情報を取り出し配列に格納（正規表現re利用）
    temp_regex = re.compile(r'\d+') #気温情報のみ取り出すため
    temp_today_high_match = temp_regex.search(tempele_today_high.text)
    temp_today_low_match = temp_regex.search(tempele_today_low.text)
    weather_info_array = [temp_today_high_match.groups(),temp_today_low_match.groups(),weather_today.text]
    
    #終了
    print("天気情報取得OK.")
    return weather_info_array
