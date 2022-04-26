import time, math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
link = 'http://suninjuly.github.io/selects1.html'

try:
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    num_1 = int(driver.find_element_by_id('num1').text)
    num_2 = int(driver.find_element_by_id('num2').text)
    print(num_1 + num_2)
    select = Select(driver.find_element_by_class_name("custom-select"))
    select.select_by_value(str(num_1+num_2))
    button = driver.find_element_by_class_name("btn-default")
    button.click()
finally:
    time.sleep(10)
    driver.quit()