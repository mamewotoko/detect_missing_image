#! /usr/bin/env python3
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlunparse, ParseResult


if __name__ == '__main__':
    user_agent = "Mozilla/5.0 (Linux; Android 4.1.2; SHL21 Build/S4011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36"
    opts = Options()
    opts.add_argument("user-agent="+user_agent)
    driver = webdriver.Chrome(chrome_options=opts)

    try:
        url = urlunparse(ParseResult(scheme='file', netloc='', path=os.path.abspath('test/missing_image.html'), params='', query='', fragment=''))
        driver.get(url)
        driver.save_screenshot('chrome_screenshot.png')
        for line in driver.get_log('browser'):
            print(line['message'])
    finally:
        driver.close()
