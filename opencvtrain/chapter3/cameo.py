import cv2
import filters
from managers import WindowManager, CaptureManager


class Cameo(object):


    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._capturManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

        self._curveFilter = filters.BGRprotraCurveFilter()