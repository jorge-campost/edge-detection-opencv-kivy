from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from params.params_service import ParamsService


class Controls(BoxLayout):
    sobel_button = ObjectProperty(None)
    canny_button = ObjectProperty(None)

    params_service = ParamsService()

    def press(self, method: str):
        self.params_service.params_observable.params.edge_detection_method = method
        self.params_service.params_observable.notify_observers()
