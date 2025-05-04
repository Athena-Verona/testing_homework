from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()
    browser.execute_script("window.scrollBy(0, 300);")

    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    result = str(math.log(abs(12 * math.sin(x))))

    inputAnswer = browser.find_element(By.ID, "answer")
    inputAnswer.send_keys(result)

    browser.execute_script("window.scrollBy(0, 300);")
    buttClick = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    buttClick.click()


finally:
    browser.quit() # quit all browser’s windows