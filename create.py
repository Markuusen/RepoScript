import sys
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

path = "PATH_TO_FILE "
browser = webdriver.Chrome()
browser.get('http://github.com/login')

username = 'USERNAME'
password = 'PASSWORD'

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    python_button = browser.find_elements(By.XPATH, "//input[@name='login']")[0]
    python_button.send_keys(username) 
    python_button = browser.find_elements(By.XPATH, "//input[@name='password']")[0] 
    python_button.send_keys(password)
    python_button = browser.find_elements(By.XPATH, "//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new') 
    python_button = browser.find_elements(By.XPATH, "//input[@name='repository[name]']")[0] 
    python_button.send_keys(folderName)
    try:
        element = WebDriverWait(browser, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#new_repository > div.js-with-permission-fields > button"))
        )
        element.click()
    except:
        element.quit()
    browser.quit()

if __name__ == "__main__":
    create()