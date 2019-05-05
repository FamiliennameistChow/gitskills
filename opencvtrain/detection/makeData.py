import sys
import numpy as np
import cv2

resize_img_y = 56  # resize training sample
resize_img_x = 56
img = cv2.imread('training.png')
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

# ***********find contours**************
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
samples = np.empty((0, resize_img_y*resize_img_x),np.float32)
responses = []
keys = [i for i in range(50, 52)]
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(thresh, (x, y), (x + w, y + h), (255, 0, 0), 1)
    roi = thresh[y:y+h, x:x+w]
    roi_resize = cv2.resize(roi, (resize_img_y, resize_img_x))
    cv2.imshow("norm", thresh)
    key = cv2.waitKey(0)
    if key == 27:  # 等待用户按下ESC(ASCII 码为27)
        sys.exit()
    elif key in keys:
        responses.append(int(chr(key)))
        sample = roi_resize.reshape((1, resize_img_y*resize_img_x))
        samples = np.append(samples, sample, 0)

responses = np.array(responses, np.float32)
responses = responses.reshape(responses.size, 1)
print("training data sucessful")

np.savetxt('generalsamples.data', samples)
np.savetxt('generalresponses.data', responses)
# fs = cv2.FileStorage('generalsamples.yml', cv2.FileStorage_WRITE)
# fs.write('samples', samples)
# fs.release()
# fs2 = cv2.FileStorage('generalresponses.yml', cv2.FileStorage_WRITE)
# fs2.write('responses', responses)
# fs2.release()


