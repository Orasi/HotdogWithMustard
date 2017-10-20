import requests
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.TestStep import TestStep

from Helpers.BasePage import BasePage
from time import sleep

from Helpers.BaseWebElement import BaseWebElement


class Footer(BaseWebElement):

    _link = (By.TAG_NAME, 'a')

    @property
    @TestStep('Find Footer Link')
    def link(self):
        return self.find('_link')


class BrokenImage(BasePage):

    sync_element = (By.CLASS_NAME, "example")

    _header = (By.TAG_NAME, 'h3')
    _img1 = (By.CSS_SELECTOR, 'img[src="asdf.jpg"]')
    _img2 = (By.CSS_SELECTOR, 'img[src="hjkl.jpg"]')
    _img3 = (By.CSS_SELECTOR, 'img[src="img/avatar-blank.jpg"]')
    _footer = (By.ID, 'page-footer')

    @TestStep('Find Link With Text - {args[1]}')
    def link(self, title):
        return self.driver.find_element(by = By.XPATH, value = "//a[text()='%s']" % title)

    @TestStep('Click on Link with title {args[1]}')
    def click_on_link(self, title):
        return self.link(title).click()

    @property
    @TestStep('Find Footer')
    def footer(self):
        return self.find('_footer', Footer)


    @property
    @TestStep('Get Header Text', True)
    def header_text(self):
        return self.find('_header').text

    @property
    @TestStep('Find First Image')
    def image1(self):
        return self.find('_img1')

    @property
    @TestStep('Find Second Image')
    def image2(self):
        return self.find('_img2')

    @property
    @TestStep('Find Third Image')
    def image3(self):
        return self.find('_img3')

    @TestStep('Check if image is displayed - {args[1].get_attribute("src")}')
    def image_displayed(self, img):
        r = requests.get(img.get_attribute('src'))
        assert r.status_code == 200, 'Image [%s] not displayed' % img.get_attribute('src')


