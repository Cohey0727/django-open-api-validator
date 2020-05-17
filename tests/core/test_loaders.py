import os
import unittest
from django_open_api_validator.core.loaders import yaml_loader

TEST_FILE_PATH = f'{os.getcwd()}/tests/spec.yml'


class LoadersTestCase(unittest.TestCase):
    def test_something(self):
        path = yaml_loader(TEST_FILE_PATH)
        self.assertEqual(TEST_FILE_PATH, path)


if __name__ == '__main__':
    unittest.main()
