import itertools
import re
from typing import Pattern

from .path_encoders import path_to_regex
from ..helpers import find

__all__ = ['Operation']


class Operation(object):
    def __init__(self, path, method, in_path_parameters, parameters=None):

        if not path.endswith('/'):
            path += '/'

        self.path = path
        self.method = method.lower()
        self.in_path_parameters = in_path_parameters
        self.parameters = parameters
        self.path_pattern = path_to_regex(path, in_path_parameters, parameters)

    def match(self, method: str, path: str) -> bool:
        if not path.endswith('/'):
            path += '/'

        return method.lower() == self.method and self.path_pattern.match(path) is not None
