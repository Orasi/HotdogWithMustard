import time
from hotdog.Retry import Retry
import os
from Helpers.FilePath import get_full_path
from Helpers.BaseWebElement import BaseWebElement
from Helpers.BaseDriver import BaseDriver

os.environ['PROJECTFOLDER'] = get_full_path('')
import builtins
from hotdog.BaseTest import HotDogBaseTest
from hotdog.Config import GetConfig

import base64,requests

class BaseTest(HotDogBaseTest):

    DefaultWebDriver = BaseDriver
    page_url = GetConfig('APP_URL')

