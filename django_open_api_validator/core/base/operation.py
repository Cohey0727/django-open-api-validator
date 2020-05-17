import itertools
import re
from typing import Pattern
from pydash import find

__all__ = ['Operation']


class Operation(object):
    def __init__(self, path, method, in_path_parameters, parameters=None):
        self.path = path
        self.method = method.lower()
        self.in_path_parameters = in_path_parameters
        self.parameters = parameters
        self.path_regex = path_to_regex(path, in_path_parameters, parameters)

    def match(self, http_method: str, url: str) -> bool:
        return http_method.lower() == self.path and self.path_regex.match(url)


def path_to_regex(path, in_path_parameters, parameters) -> Pattern[str]:
    if not in_path_parameters:
        return re.compile(path)

    a = find(parameters, lambda parameter: parameter['name'] == 'organization_id')
    b = find(parameters, lambda parameter: parameter['name'] == 'organization_name')
    print(a)
    print(b)
    pattern = path.format(**{
        in_path_parameter: find(parameters, lambda parameter: parameter['name'] == in_path_parameter)['schema'][
            'example'] for
        in_path_parameter in in_path_parameters
    })

    print(pattern)

    return re.compile(pattern)


def parameter_to_patter():
    pass
