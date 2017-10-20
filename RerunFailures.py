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
from Helpers.LoginDatabase import get_last_login



from appium_selector.DeviceSelector import DeviceSelector

MustardKey = GetConfig('MUSTARD_KEY')
MustardURL = GetConfig('MUSTARD_URL') + 'executions/%s/failing' % MustardKey


os.environ['AddMustard'] = 'True'

r = requests.get("https://api.clmustard.orasi.com/executions/cd9f1810948838f24d79c4f2598d94bc/failing")

builtins.threadlocal = threading.local()
failed_tests = json.loads(r.content.decode("utf-8") )



def run_test(device=None, test=None):

    login = get_last_login()
    builtins.threadlocal.login = login[0]
    builtins.threadlocal.password = login[1]
    builtins.threadlocal.config = device
    builtins.threadlocal.driver = None

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

def test_id(test_name):
    return test_name.split('_')[-1]


threads =[]
devices = DeviceSelector(True, platform='desktop').getDevice()
for device in devices:
    tests_to_run = []
    for t in failed_tests:
        if t['environment_id'] == device['options']['deviceName'].replace('.',''):
            tests_to_run.append("%s" % t['validation_id'])

    random.shuffle(tests_to_run)
    loader = unittest.TestLoader()
    tests = loader.discover('./Tests', pattern='*Tests.py')
    tcs = [y for x in[y for x in test_name(tests) for y in x] for y in x]
    for tc in tcs:
        if test_id(tc._testMethodName) in tests_to_run:
            t = threading.Thread(target=run_test, args=[device, tc])
            threads.append(t)
            t.start()
