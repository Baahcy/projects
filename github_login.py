''' 
 Webdriver script that logs into a Github account
 To use this, insert your Github username and password
 into the login_field_element.send_keys("") and the
 password_field.send_keys("") functions
 '''


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
import unittest
import time

class GitHubLogin(unittest.TestCase):
    def setUp(self):
        global driver 
        driver = webdriver.Firefox()
        driver.get("https://github.com/")
        driver.maximize_window()

    def test_Login(self):
        login_button_text = "Sign in"
        login_page_element = WebDriverWait(driver,10).\
                     until(lambda driver:
                        driver.find_element_by_link_text(login_button_text))
        login_page_element.click()
        assert "Sign in to GitHub" in driver.title

        login_field = "login_field"
        login_field_element = WebDriverWait(driver,10).\
                              until(lambda driver:
         driver.find_element_by_id(login_field))
        #Insert username
        login_field_element.send_keys("")
        password_field = driver.find_element_by_id("password")
        #Insert password
        password_field.send_keys("")
        login_button = driver.find_element_by_class_name("btn")
        login_button.click()
        time.sleep(5)


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()