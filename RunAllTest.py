import os
from Helpers.FilePath import get_full_path
import unittest
import threading
import builtins

os.environ['PROJECTFOLDER'] = get_full_path('')

from appium_selector.DeviceSelector import DeviceSelector


os.environ['AddMustard'] = 'True'


builtins.threadlocal = threading.local()

def run_all_test(device=None):
    builtins.threadlocal.config = device
    builtins.threadlocal.driver = None
    builtins.threadlocal.keepSession = False
    loader = unittest.TestLoader()

    tests = loader.discover('./Tests', pattern='*Tests.py')
    runner = unittest.TextTestRunner()
    runner.run(tests)

threads =[]
for device in DeviceSelector(True, platform='desktop').getDevice(filter='.*Sauce.*'):
    t = threading.Thread(target=run_all_test, args=[device])
    threads.append(t)
    t.start()

