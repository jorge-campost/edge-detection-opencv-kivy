from .params import Params
from .params_observable import ParamsObservable


def singleton(cls):
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap


@singleton
class ParamsService:
    params_observable = ParamsObservable(Params(3, "sobel"))
