import itertools
import re
from typing import Pattern

from django.conf import settings
from jsonschema import validate, draft7_format_checker
from rest_framework.response import Response

from .exceptions import exception_handler
from .path_encoders import create_path_pattern
from ..helpers import find

__all__ = ['Operation']


class Operation(object):
    def __init__(self, root, path, method, in_path_parameters, parameters=None, responses=None):

        if not path.endswith('/'):
            path += '/'

        self.root = root
        self.path = f'{getattr(settings, "DRF_OAV_SERVER_URL", "")}/{path}'
        self.method = method.lower()
        self.in_path_parameters = in_path_parameters
        self.parameters = parameters
        self.responses = responses
        self.path_pattern = create_path_pattern(path, in_path_parameters, parameters)

    def match(self, method: str, full_path: str) -> bool:
        if not full_path.endswith('/'):
            full_path += '/'

        return method.lower() == self.method and self.path_pattern.match(full_path) is not None

    @exception_handler
    def validate_response(self, response: Response, errors=None):
        if settings is None:
            errors = getattr(settings, 'OPEN_API_VALIDATOR_ERRORS', 'strict')

        schema = self.responses[str(response.status_code)]['content'][response.content_type]['schema']
        validate(instance=response.data, schema=schema, format_checker=draft7_format_checker)

    @exception_handler
    def validate_request(self, request):
        pass
