import logging
from django.conf import settings
import traceback
import time
from collections import defaultdict

from django.http import HttpRequest

from drf_open_api_validator.core.exceptions import SchemaUndefined, exception_handler
from drf_open_api_validator.core.loaders import load_schema_from_yaml
from drf_open_api_validator.core.operation import Operation
from drf_open_api_validator.helpers import find


class SchemaValidatorMiddleware(object):

    def __init__(self, get_response):
        self.operations = load_schema_from_yaml(settings.DRF_OAV_SCHEMA_FILE_PATH)
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        operation = self.get_operation(request)
        operation and operation.validate_request(request)
        response = self.get_response(request)
        operation and operation.validate_response(response)
        return response

    @exception_handler
    def get_operation(self, request: HttpRequest) -> Operation:
        operation = find(
            self.operations,
            lambda _operation: _operation.match(request.method, request.get_full_path(force_append_slash=True))
        )

        if operation is None:
            raise SchemaUndefined(request)

        return operation
