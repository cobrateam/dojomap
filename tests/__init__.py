import os
import subprocess
from urllib import urlopen

APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BASE_URL = "http://localhost:8080/"
get_url = lambda path: "%s%s" % (BASE_URL, path.lstrip("/"))

class Environment(object):
    """Dummy class for data storage"""
    pass

env = Environment()

def wait_until_server_start():
    while True:
        try:
            urlopen(BASE_URL)
            break
        except IOError:
            pass

def wait_until_server_stop():
    while True:
        try:
            response = urlopen(BASE_URL)
            if response.code == 404:
                break
        except IOError:
            break

def setup():
    output = open('/dev/null', 'w')
    env.server_process = subprocess.Popen(['python2.5', '/usr/local/google_appengine/dev_appserver.py', '--clear_datastore', APP_PATH], stdout=output, stderr=output)
    wait_until_server_start()

def teardown(total):
    subprocess.call(['kill' , '-9', '%d' % env.server_process.pid])
    wait_until_server_stop()
