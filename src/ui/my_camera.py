from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2 as cv

from params.params_service import ParamsService
from params.params_observable import ParamsObservable
from lib.observer import Observer


class MyCamera(Image, Observer):

    def __init__(self, **kwargs):
        super(MyCamera, self).__init__(**kwargs)

        # Add observer
        self.params_service = ParamsService()
        self.params_service.params_observable.add_observer(self)

        # Get the default params
        self.params = self.params_service.params_observable.params

        # Video source logic
        self.fps = 24
        self.cap = cv.VideoCapture(0)
        if not self.cap.isOpened():
            self.texture = None
            self.source = "assets/no_camera.jpg"
        else:
            Clock.schedule_interval(self.update_camera_view, 1.0 / self.fps)

    def update_camera_view(self, dt):
        ret, frame = self.cap.read()
        if ret:
            # Process image
            frame = self.process_image(
                self.params.kernel_size, self.params.edge_detection_method, frame
            )

            # Convert frame to texture
            buffer = cv.flip(frame, 0).tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt="bgr"
            )
            image_texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")

            # Display image from texture
            self.texture = image_texture

    def update(self, observable: ParamsObservable, *args, **kwargs):
        self.params = observable.params

    def process_image(
        self, kernel_size: int, method: str, frame: cv.typing.MatLike
    ) -> cv.typing.MatLike:

        # Convert to gray scale
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Blur the image for better edge detection
        img_blur = cv.GaussianBlur(img_gray, (kernel_size, kernel_size), 0)

        # Apply edge detection method
        if method == "sobel":
            res = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
        elif method == "canny":
            res = cv.Canny(image=img_blur, threshold1=100, threshold2=200)
        else:
            res = img_blur

        # Rescaling
        img_8u = cv.convertScaleAbs(res)

        # Convert gray to BGR
        return cv.cvtColor(img_8u, cv.COLOR_GRAY2BGR)
