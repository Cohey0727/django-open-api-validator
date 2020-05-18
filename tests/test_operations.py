import os
import unittest

from django.http import HttpRequest

from drf_open_api_validator.core.loaders import load_schema_from_yaml

TEST_FILE_PATH = f'{os.getcwd()}/tests/spec.yml'


class LoadersTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.operations = load_schema_from_yaml(TEST_FILE_PATH)

    def test_match(self):
        request = HttpRequest()
        self.assertTrue(self.operations[0].match('get', '/organizations/1'))
        self.assertTrue(self.operations[0].match('get', '/organizations/2/'))
        self.assertFalse(self.operations[0].match('get', '/organizations/1a'))
        self.assertFalse(self.operations[0].match('get', '/organizations/1/1'))
        self.assertFalse(self.operations[0].match('get', '/organizations/a'))
        self.assertFalse(self.operations[0].match('get', '/organizations/a/'))
        self.assertFalse(self.operations[0].match('get', '/organizations/a/1'))

    def test_validate_response(self):
        from rest_framework.response import Response
        from django.conf import settings
        settings.configure()

        response = Response(
            {
                "status": "success",
                "data": {
                    "id": 691955718,
                    "org_code": "asda",
                    "name": "hokan",
                    "email": "m.obana@hkn.jp",
                    "is_payment_failed": False,
                    "zip": "100-0004",
                    "address": "東京都千代田区大手町1-6-1 4階q",
                    "tel": "03-1234-5678",
                    "representative_position": "string",
                    "representative_name": "string",
                    "trial_end_at": '2019-09-30T09:45:49+09:00',
                    "created_at": "2019-09-30T09:45:49+09:00",
                    "updated_at": "2019-09-30T09:45:49+09:00",
                    "stripe_card_id": "card_1CfLEAE46yzLVzZozvKm6Eik",
                    "plan_id": 2
                }
            },
            status=200, content_type='application/json'
        )
        self.operations[0].validate_response(response)


if __name__ == '__main__':
    unittest.main()
