from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


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
    #天気情報を取り出し配列に格納
    
    weather_info_array = [tempele_today_high.text[0:2],tempele_today_low.text[0:2],weather_today.text]
    print("天気情報取得OK.")
    return weather_info_array
