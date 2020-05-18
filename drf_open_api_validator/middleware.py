import logging
from django.conf import settings
import traceback
import time
from collections import defaultdict

from django.http import HttpRequest

from drf_open_api_validator.core.errors import SchemaUndefined
from drf_open_api_validator.core.loaders import load_schema_from_yaml
from drf_open_api_validator.core.operation import Operation
from drf_open_api_validator.helpers import find

logger = logging.getLogger(__name__)


class SchemaValidatorMiddleware(object):

    def __init__(self, get_response):
        self.operations = load_schema_from_yaml(settings.DRF_OAV_SCHEMA_FILE_PATH)
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        operation = self.get_operation(request)
        self.validate_request(request, operation)
        response = self.get_response(request)
        self.validate_response(response, operation)
        return response

    def get_operation(self, request: HttpRequest) -> Operation:
        operation = find(
            self.operations,
            lambda _operation: _operation.match(request.method, request.get_full_path(force_append_slash=True))
        )
        # if operation is None:
        #     raise SchemaUndefined(request)

        return operation

    @staticmethod
    def validate_request(request: HttpRequest, operation: Operation):
        pass

    @staticmethod
    def validate_response(response, operation):
        try:
            operation.validate_response(response)
        except SchemaUndefined as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)
