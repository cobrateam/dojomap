from splinter.browser import Browser
from tests import env

def setup():
    env.browser = Browser('webdriver.firefox')

def teardown():
    env.browser.quit()
