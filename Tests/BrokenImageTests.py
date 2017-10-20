from Helpers.BaseTest import BaseTest
from Pages.BrokenImage import BrokenImage
from Pages.Home import HomePage
from time import sleep

class ContinuePlayingTests(BaseTest):

    def setUp(self):
        super().setUp()

        # Get url and initialize page objects
        self.driver.get(self.page_url)
        home_page = HomePage(driver=self.driver)
        self.broken_image = BrokenImage(driver=self.driver)

        home_page.sync(20)
        home_page.click_on_link('Broken Images')

        self.broken_image.sync()


    def test_broken_images(self):
        self.testcase_id = 2
        step = self.add_test_step('Validate Images are Displayed')
        self.broken_image.image_displayed(self.broken_image.image3)
        self.broken_image.image_displayed(self.broken_image.image2)
        self.broken_image.image_displayed(self.broken_image.image1)
        step('complete')

    def test_broken_image_page_loads(self):
        self.testcase_id = 3

        text = self.broken_image.header_text

        step = self.add_test_step('Validate Header Text')
        assert text == 'Broken Images', 'Header text does not match expected. Expected [%s].   Actual [%s]' % (text, 'Broken Images')
        step('complete')

    def test_footer_link_present(self):
        self.testcase_id = 1
        step = self.add_test_step('Validate Footer Link Displayed')
        assert self.broken_image.footer.link.is_displayed(), 'Footer link not displayed'
        step('complete')


