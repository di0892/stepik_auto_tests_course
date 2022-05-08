from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def sum(num1_x, num2_x):
    return str(int(num1_x) + int(num2_x))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_css_selector("[id='num1']")
    num1_x = num1.text
    num2 = browser.find_element_by_css_selector("[id='num2']")
    num2_x = num2.text
    int(num1_x)
    int(num2_x)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum(int(num1_x), int(num2_x))) 
    select.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла