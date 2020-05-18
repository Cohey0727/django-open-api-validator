from typing import List

import yaml
import re

from .exceptions import exception_handler
from .operation import Operation

__all__ = ['load_schema_from_yaml']


@exception_handler
def load_schema_from_yaml(path_to_yaml: str) -> List[Operation]:
    res = []
    with open(path_to_yaml, 'r') as file:
        reg = r'(?<={).*?(?=})'
        spec = yaml.load(file, Loader=yaml.SafeLoader)
        for path, methods in spec['paths'].items():
            in_path_parameters = re.findall(reg, path)
            res += [
                Operation(spec, path, method, in_path_parameters, payload.get('parameters'), payload.get('responses'))
                for method, payload in methods.items()
            ]

    return res
