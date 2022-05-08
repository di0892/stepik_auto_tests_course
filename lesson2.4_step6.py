from selenium import webdriver
import time

link = "http://suninjuly.github.io/cats.html?"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_id("button")
    button1.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла