from django.http import HttpRequest


class SchemaUndefined(Exception):
    def __init__(self, request: HttpRequest):
        super().__init__(f'Schema <{request.get_full_path()} {request.method}> is undefined.')
