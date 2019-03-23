# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver
import time

phantomjs_path = "/root/phantomjs"
url = "http://127.0.0.1/robots_api_2333.php"
browser = webdriver.PhantomJS(executable_path = phantomjs_path)
browser.add_cookie({'name': 'auth', 'value': 'haozigege', 'path': '/', 'domain': '.127.0.0.1'}) 
while True:
    try:
        browser.get(url)
        print "[*] Request success."
        time.sleep(5) 
    except Exception as e:
        print "[!] Error: " + str(e)
        continue
