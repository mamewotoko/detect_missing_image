Detect missing image in HTML
=============================
Detect missing image in HTML using google chrome web driver.

Prepare
---------
1. Install the latest chrome driver
2. Install python3

Run
----
1. run following command

```
./missing_image.py
```

2. browser log is diplayed to stdout

```
file:///Users/xxx/dtect_missing_image/test/hello.png - Failed to load resource: net::ERR_FILE_NOT_FOUND
```

chrome_screenshot.png is screen capture of chrome.

Reference
---------
* [SeleniumでChromeのデベロッパーツール相当の機能を使ってみよう](https://qiita.com/okitan/items/ee6f5094319b964e84e1#console-log%E3%81%AE%E5%8F%96%E5%BE%97)
* [7. WebDriver API](http://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.get_log)
