import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def fill_form(self, link):
        self.browser.get(link)

        inputName = self.browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        inputName.send_keys("Petras")

        inputLastName = self.browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        inputLastName.send_keys("Petrauskas")

        inputEmail = self.browser.find_element(By.XPATH, "//label[text()='Phone:']/following-sibling::input")
        inputEmail.send_keys("0000000000")

        inputPost = self.browser.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
        inputPost.send_keys("Lithuania")

        inputCountry = self.browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        inputCountry.send_keys("Petrauskas@gmail.com")

        buttClick = self.browser.find_element(By.CLASS_NAME, "btn.btn-default")
        buttClick.click()

        success_message = self.browser.find_element(By.TAG_NAME, "h1").text
        return success_message

    def test1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        success_message = self.fill_form(link1)
        self.assertEqual(success_message, "Congratulations! You have successfully registered!")

    def test2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        success_message = self.fill_form(link2)
        self.assertEqual(success_message, "Congratulations! You have successfully registered!")  #will fail

if __name__ == "__main__":
    unittest.main()