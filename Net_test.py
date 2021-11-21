from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def network_test():
    network_ok = 0
    option = Options()                          # オプションを用意
    option.add_argument('--headless')           #ブラウザをひらかず
    CHROME_DRIVER = '/usr/lib/chromium-browser/chromedriver'
    browser = webdriver.Chrome(CHROME_DRIVER,options=option)
    url_id = "https://www.google.co.jp"
    while network_ok != 1:
        try:
            browser.get(url_id)
            network_ok = 1
        except:
            network_ok = 0