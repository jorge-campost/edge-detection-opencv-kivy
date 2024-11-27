from lib.observable import Observable
from .params import Params


class ParamsObservable(Observable):

    def __init__(self, params: Params):
        super().__init__()
        self.params = params

    def set_params(self, params: Params):
        self.params = params
        self.notify_observers()

    def set_param(self, key: str, value):
        self.params[key] = value
        self.notify_observers()
