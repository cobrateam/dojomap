import unittest
from dojomap import app

class TestDojoViews(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_add_dojo_view(self):
        "Should contain a view that responds to URL /dojo/new"
        with app.test_request_context():
            response = self.client.get("/dojo/new")
            assert response.status_code == 200
