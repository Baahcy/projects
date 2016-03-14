from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import unittest
import time

class SwitchToFrame(unittest.TestCase):

    def setUp(self):
        global driver 
        driver = webdriver.Firefox()
        driver.get("http://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        driver.maximize_window()

    def test_SwitchToFrame(self):
        #Locators
        iFrameID = "iframeResult"
        tryItButtonLocator = "//button[.='Try it']"
        iFrameElement = WebDriverWait(driver, 10).\
        until(lambda driver: driver.find_element_by_id(iFrameID))

        driver.switch_to_frame(iFrameElement)

        tryItButtonElement = WebDriverWait(driver, 10).\
        until(lambda driver: driver.find_element_by_xpath(tryItButtonLocator))

        tryItButtonElement.click()

        #time.sleep(6)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()