import cv2
import filters
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()  # new add

    def run(self):
        ''' Run the mian loop '''
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            filters.strokeEdges(frame, frame)    # new add
            self._curveFilter.apply(frame, frame)   # new add

            # TODO：Filter the frame(Chapter 3)
            self._captureManager.exitFrame()
            self._windowManager.processEventes()

    def onKeypress(self, keycode):
        '''Handle a keypress
        space -> Take a screenshot
        tab -> start/stop recording a screencast
        escape -> Quit
        '''

        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode ==9: #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()


if __name__ == '__main__':
    Cameo().run()