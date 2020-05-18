from django.http import HttpRequest
import logging

logger = logging.getLogger(__name__)

__all__ = [
    'exception_handler', 'SchemaUndefined'
]


def exception_handler(func):
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            return None

    return decorator


class SchemaUndefined(Exception):
    def __init__(self, request: HttpRequest):
        super().__init__(f'Schema <{request.get_full_path()} {request.method}> is undefined.')
