from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.TestStep import TestStep

from Helpers.BasePage import BasePage
from time import sleep

class HomePage(BasePage):

    sync_element = (By.CLASS_NAME, "heading")


    def link(self, title):
        return self.driver.find_element(by = By.XPATH, value = "//a[text()='%s']" % title)

    @TestStep('Click on Link with title {args[1]}')
    def click_on_link(self, title):
        self.link(title).click()

