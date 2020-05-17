import itertools
import re
from typing import Pattern

from .path_encoders import path_to_regex
from ..helpers import find

__all__ = ['Operation']


class Operation(object):
    def __init__(self, path, method, in_path_parameters, parameters=None):
        self.path = path
        self.method = method.lower()
        self.in_path_parameters = in_path_parameters
        self.parameters = parameters
        self.path_regex = path_to_regex(path, in_path_parameters, parameters)

    def match(self, http_method: str, url: str) -> bool:
        return http_method.lower() == self.method and self.path_regex.match(url) is not None


