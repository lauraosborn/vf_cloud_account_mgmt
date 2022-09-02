import unittest
from flask import current_app
from vf_cloud_account_mgmt import create_vf_cloud_account_mgmt


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.vf_cloud_account_mgmt = create_vf_cloud_account_mgmt()
        self.vf_cloud_account_mgmtctx = self.vf_cloud_account_mgmt.vf_cloud_account_mgmt_context()
        self.vf_cloud_account_mgmtctx.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.vf_cloud_account_mgmtctx.pop()
        self.vf_cloud_account_mgmt = None
        self.vf_cloud_account_mgmtctx = None

    def test_app(self):
        assert self.vf_cloud_account_mgmt is not None
        assert current_vf_cloud_account_mgmt == self.vf_cloud_account_mgmt

    def test_registration_form(self):
        response = self.client.get('/new_account')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # make sure all the fields are included
        assert 'name="accountID"' in html
        assert 'name="accountName"' in html
        assert 'name="csp"' in html
        assert 'name="accountOwner"' in html
        assert 'name="accountOwner"' in html