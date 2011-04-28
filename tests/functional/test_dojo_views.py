import unittest
from dojomap import app
from dojomap.models import Dojo
from nose.tools import assert_equals

class TestDojoViews(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_add_dojo_view(self):
        "Should contain a view that responds to URL /dojo/new"
        with app.test_request_context():
            response = self.client.get("/dojo/new")
            assert_equals(response.status_code, 200)

    def test_create_dojo_view(self):
        "Should contain a view that creates a dojo on database on POST requests"
        with app.test_request_context():

            post_data = {
                'name' : u'Main dojo',
                'description' : u'The main dojo of the entire universe',
                'address' : u'Main street, 20'
            }

            response = self.client.post("/dojo/new", data=post_data, follow_redirects=True)
            assert_equals(response.status_code, 200)

            dojo = Dojo.all().filter('name =', u'Main dojo').get()
            assert_equals(dojo.address, u'Main street, 20')
