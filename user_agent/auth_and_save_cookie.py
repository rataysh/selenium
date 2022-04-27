import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import pickle # for cooke
from auth_discord import login_discord, password_discord


# # change useragent
# ua = UserAgent()
#options
options = Options()
# # options.add_argument("start-maximized")
# options.add_argument(f"user-agent={ua.chrome}")


link = 'https://discord.com/login'

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    driver.get(link)
    form_auth = driver.find_elements(By.CLASS_NAME, "inputDefault-3FGxgL")
    form_auth[0].click()
    form_auth[0].send_keys(login_discord)
    form_auth[1].click()
    form_auth[1].send_keys(password_discord)
    button_input = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_input.click()
    time.sleep(5)
    ##Создаем файл с куками
    pickle.dump(driver.get_cookies(), open("cookie_discord", "wb"))
    driver.quit()
finally:
    time.sleep(3)
    driver.quit()