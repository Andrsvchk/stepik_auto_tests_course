from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def sum(x, y):
    return str(x + y)

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    y = int(y_element.text)
    summa = sum(x, y)
    from selenium.webdriver.support.ui import Select

    browser.find_element(By.CSS_SELECTOR, "#dropdown").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(summa))
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()