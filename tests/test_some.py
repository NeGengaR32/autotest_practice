import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_sale_page():
    browser = webdriver.Chrome()
    browser.get("https://magento.softwaretestingboard.com/")
    sale_button = browser.find_element(By.ID, value="ui-id-8")
    sale_button.click()
    title = browser.find_element(By.TAG_NAME, value="h1")
    assert title.text == "Sale"
    
def test_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    assert len(response) == 100