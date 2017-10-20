import os

from hotdog.TestStep import TestStep

from Helpers.FilePath import get_full_path
os.environ['PROJECTFOLDER'] = get_full_path('')
from time import sleep
from hotdog.BasePage import HotDogBasePage


class BasePage(HotDogBasePage):

    @TestStep('Scroll to End of Page')
    def scroll_to_end_of_page(self,offset=0,sleep_time=2):
        '''
        Scrolls to the end of the page dynamically. It will keep scrolling to the end of the page until
        there aren't anymore elements loaded dynamically.
        '''
        page_height = self.driver.execute_script('return document.body.scrollHeight')
        new_page_height = 0

        while page_height is not new_page_height:
            self.driver.execute_script("window.scrollTo(0, (%s))" % (page_height-offset))
            sleep(sleep_time)
            new_page_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_page_height > page_height:
                page_height = new_page_height
                new_page_height = 0
            else:
                page_height = new_page_height
            sleep(2)