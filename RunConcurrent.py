import os
import json
from hotdog.Config import GetConfig
import itertools
from Helpers.FilePath import get_full_path
import unittest
import threading
import builtins
import requests



os.environ['PROJECTFOLDER'] = get_full_path('')
from Helpers.LoginDatabase import get_last_login
from appium_selector.DeviceSelector import DeviceSelector

MustardURL = GetConfig('MUSTARD_URL') + '/incomplete'
MustardKey = GetConfig('MUSTARD_KEY')

os.environ['AddMustard'] = 'True'

r = requests.post(MustardURL, data={'project_id': MustardKey,})
threads =[]
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

def get_tests():
    tests_to_run = []
    result = []
    failed_tests = json.loads(r.content.decode("utf-8") )
    for device in DeviceSelector(True, platform='desktop').getDevice():
        for t in failed_tests:
            if t[1] == device['options']['deviceName'].replace('.',''):
                tests_to_run.append(t[0])

        builtins.threadlocal = threading.local()

        loader = unittest.TestLoader()

        tests = loader.discover('./Tests', pattern='*Tests.py')
        runner = unittest.TextTestRunner()

        tcs = [y for x in[y for x in test_name(tests) for y in x] for y in x]

        for tc in tcs:
            if tc._testMethodName in tests_to_run:
                t = threading.Thread(target=run_all_test, args=[device, tc])
                threads.append(t)

                t.start()

def run_all_test(device=None, test=None):

    builtins.threadlocal.config = device
    builtins.threadlocal.driver = None
    login = get_last_login()
    builtins.threadlocal.login = login[0]
    builtins.threadlocal.password = login[1]
    runner = unittest.TextTestRunner()
    runner.run(test)


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

get_tests()