from typing import Iterable, Callable


def find(iterable: Iterable, pred: Callable, default: bool = False):
    return next(filter(pred, iterable), default)
