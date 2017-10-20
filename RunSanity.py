import os
from Helpers.FilePath import get_full_path
os.environ['PROJECTFOLDER'] = get_full_path('')

from builtins import range
from appium_selector.DeviceSelector import DeviceSelector
from hotdog.Config import GetConfig

import unittest
import threading
import builtins
import random

    MustardURL = GetConfig('MUSTARD_URL') + '/incomplete'
MustardKey = GetConfig('MUSTARD_KEY')

os.environ['AddMustard'] = 'True'

builtins.threadlocal = threading.local()

def chunkify(lst,n):
    return [ lst[i::n] for i in range(n) ]

def run_all_test(tests, device):
    runner = unittest.TextTestRunner()
    builtins.threadlocal.config = device
    builtins.threadlocal.driver = None
    for test in tests:
        runner.run(test)

def get_all_tests():
    loader = unittest.TestLoader()
    tests = loader.discover('./Tests', pattern='*Tests.py')
    runner = unittest.TextTestRunner()
    tcs = [y for x in[y for x in test_name(tests) for y in x] for y in x]
    random.shuffle(tcs)
    return tcs

def test_name(parent):
    tns = []
    if hasattr(parent, '_testMethodName'):
        return parent
    elif hasattr(parent, '_tests'):
        for t in parent._tests:
            tn= test_name(t)
            if tn:
                tns.append( tn)
    return tns

threads =[]
tests_to_run = get_all_tests()
chunked_tests = chunkify(tests_to_run, 10)
device = DeviceSelector(True, platform='desktop').getDevice()
device[0]['options']['mustard'] = True
for test in chunked_tests:
    t = threading.Thread(target=run_all_test, args=[test, device[0]])
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

# print('finished')
# os.system('python3 RerunFailures.py')