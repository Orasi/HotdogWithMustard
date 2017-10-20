import os
import json
from hotdog.Config import GetConfig
import itertools
from Helpers.FilePath import get_full_path
import unittest
import threading
import builtins
import requests
import random
os.environ['PROJECTFOLDER'] = get_full_path('')

from appium_selector.DeviceSelector import DeviceSelector

MustardURL = GetConfig('MUSTARD_URL') + '/incomplete'
MustardKey = GetConfig('MUSTARD_KEY')

os.environ['AddMustard'] = 'True'

r = requests.post(MustardURL, data={'project_id': MustardKey,})

builtins.threadlocal = threading.local()
failed_tests = json.loads(r.content.decode("utf-8") )

def run_all_test(device=None):
    tests_to_run = []
    for t in failed_tests:
        if t[1] == device['options']['deviceName'].replace('.',''):
            tests_to_run.append(t[0])

    builtins.threadlocal.config = device
    builtins.threadlocal.driver = None
    loader = unittest.TestLoader()
    tests = loader.discover('./Tests', pattern='*Tests.py')
    runner = unittest.TextTestRunner()
    tcs = [y for x in[y for x in test_name(tests) for y in x] for y in x]
   # random.shuffle(tcs)
    for tc in tcs:
        if tc._testMethodName in tests_to_run:
            runner.run(tc)

threads =[]
for device in DeviceSelector(True, platform='desktop').getDevice():
    t = threading.Thread(target=run_all_test, args=[device])
    threads.append(t)
    t.start()

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

