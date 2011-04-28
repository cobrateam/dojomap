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
