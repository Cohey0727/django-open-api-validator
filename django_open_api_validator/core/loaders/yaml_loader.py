import yaml
import re

from django_open_api_validator.core.base.operation import Operation

__all__ = ['yaml_loader']


def yaml_loader(path_to_yaml: str):
    res = []
    with open(path_to_yaml, 'r') as file:
        reg = r'(?<={).*?(?=})'
        spec = yaml.load(file, Loader=yaml.SafeLoader)
        for path, methods in spec['paths'].items():
            in_path_parameters = re.findall(reg, path)
            print(in_path_parameters)
            res += [Operation(path, method, in_path_parameters, payload.get('parameters')) for method, payload in methods.items()]

    return path_to_yaml
