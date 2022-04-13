import time
from selenium import webdriver


chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
link = 'http://suninjuly.github.io/find_xpath_form'

value1 = 'input'
value2 = 'last_name'
value3 = 'city'
value4 = 'country'

try:
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    input1 = driver.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name(value3)
    input3.send_keys("Madrid")
    input4 = driver.find_element_by_id(value4)
    input4.send_keys("USA")
    button = driver.find_element_by_xpath("/html/body[@class='bg-light']/div[@class='container']/form/div[6]/button[@class='btn'][3]")
    button.click()
finally:
    time.sleep(10)
    driver.quit()