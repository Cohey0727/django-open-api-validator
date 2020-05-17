import os
import unittest
from django_open_api_validator.core.loaders import yaml_loader

TEST_FILE_PATH = f'{os.getcwd()}/tests/spec.yml'


class LoadersTestCase(unittest.TestCase):
    def test_something(self):
        operations = yaml_loader(TEST_FILE_PATH)
        self.assertTrue(operations[0].match('get', '/organizations/1'))


if __name__ == '__main__':
    unittest.main()
