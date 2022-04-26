import time
from selenium import webdriver

chromedriver_path = '/home/denis/chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)
link = 'http://suninjuly.github.io/wait1.html'

try:
    driver.get(link)
    button = driver.find_element_by_class_name("btn-primary")
    button.click()
except Exception:
    print('Если элемент не был найден за отведенное время, то мы получим NoSuchElementException')
    print('Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM '
          'изменился, то получим StaleElementReferenceException')
    print('Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),'
          ' то получим ElementNotVisibleException.')
finally:
    time.sleep(5)
    driver.quit()


# Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
# Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
# Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.