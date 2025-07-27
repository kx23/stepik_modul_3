import time
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_located_on_page(browser):
    browser.get(link)
    time.sleep(30)
    addButton = None
    try:
        addButton = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except NoSuchElementException:
        print("Element not found with the specified ID.")
    assert addButton != None, "Element was not found"
