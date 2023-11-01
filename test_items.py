import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_enabled()
    assert basket_button, "There is no button"
    #time.sleep(30)