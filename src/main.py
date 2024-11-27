import kivy
from kivy.app import App
from kivy.config import Config

# Check kivy version
kivy.require("2.3.0")
# Set config parameters
Config.set("graphics", "resizable", False)
Config.set("graphics", "width", 640)
Config.set("graphics", "height", 480)

from kivy.core.window import Window
from kivy.lang import Builder

# Custom classes
from ui.main_layout import MainLayout
from ui.my_camera import MyCamera
from ui.controls import Controls


def setup():
    # Load .kv files
    Builder.load_file("ui/main_layout.kv")
    Builder.load_file("ui/controls.kv")


class EdgeDetectionApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    setup()
    EdgeDetectionApp().run()
