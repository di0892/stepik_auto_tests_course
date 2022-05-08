from selenium import webdriver
import time
import math

def calc(sunduk_x):
  return str(math.log(abs(12*math.sin(int(sunduk_x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    sunduk = browser.find_element_by_css_selector("[id='treasure']")
    sunduk_x = sunduk.get_attribute("valuex")
    y = calc(sunduk_x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(sunduk_x))

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла