import re
from typing import Pattern
from ..helpers import find


def create_path_pattern(path: str, in_path_parameters, parameters) -> Pattern[str]:
    if not in_path_parameters:
        return re.compile(f'{path}$')

    pattern = path.format(**{
        in_path_parameter:
            regex_string_from_schema(
                find(parameters, lambda parameter: parameter['name'] == in_path_parameter)['schema']
            )
        for in_path_parameter in in_path_parameters
    })
    return re.compile(f'{pattern}$')


type_format_regex_string_map = {
    ('number', None): r'\d',
    ('number', 'float'): r'\d',
    ('number', 'double'): r'\d',
    ('integer', None): r'\d',
    ('integer', 'int32'): r'\d',
    ('integer', 'int64'): r'\d',
    ('string', None): r'[a-zA-Z][a-zA-Z0-9]*',
    ('string', 'date'): r'^\\d{4}-\\d{2}-\\d{2}$',
    ('string', 'date-time'): r'^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$',
    ('string', 'password'): r'\w',
    ('string', 'byte'): r'\w',
    ('string', 'binary'): r'\w',
    ('string', 'email'): r'\w',
    ('string', 'uuid'): r'\w',
    ('string', 'uri'): r'\w',
    ('string', 'hostname'): r'\w',
    ('string', 'ipv4'): r'\w',
    ('string', 'ipv6'): r'\w',
}


def regex_string_from_schema(schema: dict) -> str:
    return type_format_regex_string_map[(schema['type'], schema.get('format'))]
