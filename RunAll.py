import requests
from hotdog.Config import GetConfig

from Helpers.FilePath import get_full_path
import unittest
import threading
import builtins
import os

os.environ['PROJECTFOLDER'] = get_full_path('')
from appium_selector.DeviceSelector import DeviceSelector

MustardURL = GetConfig('MUSTARD_URL').replace('results', 'executions') + '/close'
MustardKey = GetConfig('MUSTARD_KEY')

# r = requests.post(MustardURL, data={'project_key': MustardKey,})

os.environ['AddMustard'] = 'True'

builtins.threadlocal = threading.local()

def run_all_test(device=None):
    builtins.threadlocal.config = device
    builtins.threadlocal.driver = None
    builtins.threadlocal.keepSession = False
    loader = unittest.TestLoader()

    tests = loader.discover('./Tests/', pattern='*Tests.py')
    runner = unittest.TextTestRunner()
    runner.run(tests)

threads =[]
for device in DeviceSelector(True, platform='desktop').getDevice():
    t = threading.Thread(target=run_all_test, args=[device])
    threads.append(t)
    t.start()

