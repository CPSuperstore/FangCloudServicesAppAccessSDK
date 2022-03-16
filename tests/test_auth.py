import unittest
import sys
import json

sys.path.append('..')

from FCSAppAccess import *

with open("../credentials.json") as f:
    credentials = json.load(f)


class TestCaseComparisons(unittest.TestCase):
    def test_correct_credentials(self):
        FCSAppAccess(
            credentials["client_id"], credentials["client_secret"], "*:*:*"
        ).client_credentials()

    def test_expired_access_token(self):
        access = FCSAppAccess(
            credentials["client_id"], credentials["client_secret"], "*:*:*"
        )

        access.set_access_token(credentials["expired_access"], credentials["expired_refresh"])
        access.refresh_token()

    def test_incorrect_credentials(self):
        self.assertRaises(
            InvalidGrantException,
            lambda: FCSAppAccess(
                credentials["client_id"] + "BAD", credentials["client_secret"], "*:*:*"
            ).client_credentials()
        )

    def test_device_code(self):
        access = FCSAppAccess(
            credentials["client_id"], credentials["client_secret"], "*:*:*"
        )
        device_code = access.device_code()
        print(device_code.verification_uri_full)
        print(access.device_code_poll(device_code))


if __name__ == '__main__':
    unittest.main()
