import time, math
from selenium import webdriver


chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
link = 'http://suninjuly.github.io/math.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    value_x = driver.find_element_by_id("input_value").text
    result_math = calc(value_x)
    input_form = driver.find_element_by_class_name("form-control")
    input_form.send_keys(result_math)
    not_a_human = driver.find_element_by_id("robotCheckbox")
    not_a_human.click()
    not_a_human = driver.find_element_by_id("robotsRule")
    not_a_human.click()
    button = driver.find_element_by_class_name("btn-default")
    button.click()
finally:
    time.sleep(10)
    driver.quit()