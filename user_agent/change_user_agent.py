import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

# from seleniumwire import webdriver
from fake_useragent import UserAgent


# change useragent
ua = UserAgent()

#options
options = Options()
# options.add_argument("start-maximized")
options.add_argument(f"user-agent={ua.random}")


link = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'


try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(link)
    time.sleep(3)
    driver.quit()
finally:
    time.sleep(3)
    driver.quit()