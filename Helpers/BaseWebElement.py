from hotdog.BaseElement import BaseElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseWebElement(BaseElement):

    def is_element_visible(self):
        return self.driver.execute_script(
            'function isElementInViewPort(el) { '
                'var rect = el.getBoundingClientRect(); '
                'return (rect.bottom >= 0 && rect.right >= 0 && rect.top <= '
                    '(window.innerHeight || document.documentElement.clientHeight) && '
                    'rect.left <= (window.innerWidth || document.documentElement.clientWidth));'
            '}'
            'function isOverflowed(el) {'
                'return el.scrollHeight > el.clientHeight || el.scrollWidth > el.clientWidth;'
            '}'
            'return isElementInViewPort($(arguments[0])[0]) && isOverflowed($(arguments[0])) == false', self)