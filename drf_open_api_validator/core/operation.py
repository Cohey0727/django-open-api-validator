import itertools
import re
from typing import Pattern

from django.conf import settings
from jsonschema import validate
from rest_framework.response import Response

from .path_encoders import create_path_pattern
from ..helpers import find

__all__ = ['Operation']


class Operation(object):
    def __init__(self, root, path, method, in_path_parameters, parameters=None, responses=None):

        if not path.endswith('/'):
            path += '/'

        self.root = root
        self.path = path
        self.method = method.lower()
        self.in_path_parameters = in_path_parameters
        self.parameters = parameters
        self.responses = responses
        self.path_pattern = create_path_pattern(path, in_path_parameters, parameters)

    def match(self, method: str, path: str) -> bool:
        if not path.endswith('/'):
            path += '/'

        return method.lower() == self.method and self.path_pattern.match(path) is not None

    def validate_response(self, response: Response, errors=None):
        if settings is None:
            errors = getattr(settings, 'OPEN_API_VALIDATOR_ERRORS', 'strict')

        schema = self.responses[str(response.status_code)]['content'][response.content_type]['schema']
        validate(instance=response.data, schema=schema)

    def validate_request(self, request):
        pass
