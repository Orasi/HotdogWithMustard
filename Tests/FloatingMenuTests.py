from Helpers.BaseTest import BaseTest
from Pages.BrokenImage import BrokenImage
from Pages.FloatingMenu import FloatingMenu
from Pages.Home import HomePage
from time import sleep

class FloatingMenuTests(BaseTest):

    def setUp(self):
        super().setUp()

        # Get url and initialize page objects
        self.driver.get(self.page_url)
        home_page = HomePage(driver=self.driver)
        self.floating_menu  = FloatingMenu(driver=self.driver)

        home_page.sync(20)
        home_page.link('Floating Menu').click()

        self.floating_menu.sync()


    def test_menu_home_present(self):
        self.testcase_id = 7

        step = self.add_test_step('Validate Floating Menu Is Displayed')
        assert self.floating_menu.menu.item('Home').is_displayed(), 'Floating Menu was not displayed'
        step('complete')


    def test_news_present(self):
        self.testcase_id = 8

        step = self.add_test_step('Validate Floating Menu Is Displayed')
        assert self.floating_menu.menu.item('News').is_displayed(), 'Floating Menu was not displayed'
        step('complete')


    def test_menu_contact_present(self):
        self.testcase_id = 5

        step = self.add_test_step('Validate Floating Menu Is Displayed')
        assert self.floating_menu.menu.item('Contact').is_displayed(), 'Floating Menu was not displayed'
        step('complete')


    def test_menu_about_present(self):
        self.testcase_id = 4

        step = self.add_test_step('Validate Floating Menu Is Displayed')
        assert self.floating_menu.menu.item('About').is_displayed(), 'Floating Menu was not displayed'
        step('complete')


    def test_menu_floats_after_scroll(self):
        self.testcase_id = 6

        self.floating_menu.scroll_to_end_of_page()

        step = self.add_test_step('Validate Menu Floats')
        assert self.floating_menu.menu.is_displayed(), 'Menu not floating at bottom of page'
        step('complete')

