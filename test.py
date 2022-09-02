import unittest
from flask import app
from app import create_app


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

# def test_registration_form(self):
#     response = self.client.get('/new_account')
#     assert response.status_code == 200
#     html = response.get_data(as_text=True)

#     # make sure all the fields are included
#     assert 'name="accountID"' in html
#     assert 'name="accountName"' in html
#     assert 'name="csp"' in html
#     assert 'name="accountOwner"' in html
#     assert 'name="accountOwner"' in html