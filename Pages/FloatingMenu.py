import requests
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.TestStep import TestStep

from Helpers.BasePage import BasePage
from time import sleep

from Helpers.BaseWebElement import BaseWebElement


class Menu(BaseWebElement):

    _home = (By.CSS_SELECTOR, 'a[href="#home"]')
    _news = (By.CSS_SELECTOR, 'a[href="#news"]')
    _contact = (By.CSS_SELECTOR, 'a[href="#about"]')
    _about = (By.CSS_SELECTOR, 'a[href="#contact"]')


    @TestStep('Find Menu Item - {args[1]}')
    def item(self, item):
        return self.find('_%s' % item.lower())


class FloatingMenu(BasePage):

    sync_element = (By.CLASS_NAME, "example")

    _menu = (By.ID, 'menu', Menu)

    @property
    @TestStep('Find Floating Menu')
    def menu(self):
        return self.find('_menu')

    @property
    @TestStep('Get Header Text', True)
    def header_text(self):
        return self.find('_header').text
