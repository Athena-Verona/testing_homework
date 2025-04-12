from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Firefox()
    browser.get(link)

    buttClick = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    buttClick.click()
    browser.implicitly_wait(5)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    result = str(math.log(abs(12 * math.sin(x))))

    inputAnswer = browser.find_element(By.ID, "answer")
    inputAnswer.send_keys(result)

    browser.implicitly_wait(3)
    buttClick = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    buttClick.click()
    #inputSubmit = WebDriverWait(browser, 3).until(
    #    EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-primary"))
    #)
    #inputSubmit.click()

    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    browser.implicitly_wait(3)
    alert.accept()

finally:
    browser.quit() # quit all browser’s windows
