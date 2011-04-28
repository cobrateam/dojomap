import unittest
from tests import env, get_url

class TestAddDojo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = env.browser

    def test_form_add_dojo(self):
        "Should show a form on /dojo/new url"
        self.browser.visit(get_url("/dojo/new"))
        assert self.browser.is_element_present_by_css('form#new-dojo')

    def test_unable_to_save_with_invalid_data(self):
        "Should be unable to save a dojo when providing invalid data"
        self.browser.visit(get_url("/dojo/new"))
        self.browser.find_by_css('input[type=submit]').first.click()
        assert self.browser.is_element_present_by_css('.validation-errors')
