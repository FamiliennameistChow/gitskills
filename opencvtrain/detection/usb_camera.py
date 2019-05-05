import cv2

videoCaputer = cv2.VideoCapture(1)
videoCaputer.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
videoCaputer.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    _, frame = videoCaputer.read()
    cv2.imshow("test", frame)
    if cv2.waitKey(1) == 27:
        break



# size = (int(videoCaputer.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(videoCaputer.get(cv2.CAP_PROP_FRAME_WIDTH)))
# print(size)
# _,frame = videoCaputer.read()
# print(frame.shape)