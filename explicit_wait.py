import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)
link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver.get(link)
    check_price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = driver.find_element(By.ID, "book")
    button.click()
    value_x = driver.find_element(By.ID, "input_value").text
    result_math = calc(value_x)
    form_insert = driver.find_element(By.ID, "answer")
    form_insert.send_keys(result_math)
finally:
    time.sleep(5)
    driver.quit()