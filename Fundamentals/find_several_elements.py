import time
from selenium import webdriver


chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
link = 'http://suninjuly.github.io/huge_form.html'
tag_for_serch = 'input'

try:
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    all_elements = driver.find_elements_by_tag_name(tag_for_serch)
    for each_elements in all_elements:
        each_elements.send_keys("value")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    driver.quit()