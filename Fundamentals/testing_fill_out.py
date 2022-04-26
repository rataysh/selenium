import time
from selenium import webdriver


chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
link = 'http://suninjuly.github.io/registration1.html'
class_value = 'form-control'
schetchik = 0
check_result = 'Congratulations! You have successfully registered!'

try:
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    main_blocks = driver.find_elements_by_class_name(class_value)
    for main_block in list(main_blocks[:3]):
        main_block.send_keys("value")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    welcome_text_elt = driver.find_element_by_tag_name('h1')
    welcome_text_elt = welcome_text_elt.text
    # print(welcome_text_elt)
    assert welcome_text_elt == check_result
finally:
    time.sleep(2)
    driver.quit()