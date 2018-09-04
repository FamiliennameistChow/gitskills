import cv2

'''
opencv 视频文件读取
'''

videoCapture = cv2.VideoCapture('Tensorflow.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'Tensorflow.mp4', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)

success, frame = videoCapture.read()
while success: # loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()
