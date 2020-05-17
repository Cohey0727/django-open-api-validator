import logging
import traceback
import time
from collections import defaultdict

logger = logging.getLogger(__name__)


class ResponseValidatorMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.validate(response)
        return response

    def validate(self, response):
        pass
