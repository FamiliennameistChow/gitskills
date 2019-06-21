import cv2
import numpy as np
import sys


def get_minAreaRect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    return cv2.minAreaRect(coords)


def rotate_bound(image, angle):
    # 获取宽高
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # 提取旋转矩阵 sin cos
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像的新边界尺寸
    nW = int((h * sin) + (w * cos))
    #     nH = int((h * cos) + (w * sin))
    nH = h

    # 调整旋转矩阵
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def detecte_circle(img):
    # ****************training***************
    samples = np.loadtxt('generalsamples.data', np.float32)
    responses = np.loadtxt('generalresponses.data', np.float32)
    responses = responses.reshape((responses.size, 1))
    model = cv2.ml.KNearest_create()
    model.train(samples, cv2.ml.ROW_SAMPLE, responses)

    # 灰度化
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower_red = np.array([0, 43, 46])
    # upper_red = np.array([10, 255, 255])

    lower_red = np.array([125, 50, 46])
    upper_red = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
    dst = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    cv2.waitKey()
    cv2.destroyAllWindows()
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    cv2.imshow('gray_G', gray)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # 输出图像大小，方便根据图像大小调节minRadius和maxRadius
    print(img.shape)
    # 霍夫变换圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=50
                               , maxRadius=300)

    print(circles)
    # 输出返回值，方便查看类型
    try:
        print(circles)
        # 输出检测到圆的个数
        print("number of detect circle:", len(circles[0]))

        radius = []
        for i in range(len(circles[0])):
            radius += [circles[0][i][2]]
            # print(radius)
        print("radius_list", radius)

        if len(radius) > 3:
            radius.remove(min(radius))
            radius.remove(max(radius))
            radius_mean = int(np.mean(radius))
            print(radius_mean)

            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=(radius_mean-15),
                                       maxRadius=(radius_mean+15))
            print("number of detect circle:", len(circles[0]))
    except TypeError:
        print("NO Circles found")
    else:
        # print('-------------我是条分割线-----------------')
        # 根据检测到圆的信息，画出每一个圆
        # circle_img = []
        for circle in circles[0]:
            # 坐标行列
            x = int(circle[0])
            y = int(circle[1])
            # 半径
            r = int(circle[2])
            # 剔除边界外圆
            if int(y-r/2) < 0 or int(x-r/2) < 0 or int(y+r/2) > img.shape[0] or int(x+r/2) > img.shape[1]:
                continue

            # 剔除小圆干扰
            if r < 50:
                continue

            # 圆的基本信息
            print('radius:', circle[2])
            circle_img = img[int(y-r/2):int(y+r/2), int(x-r/2):int(x+r/2)]
            cv2.imshow("corp", circle_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            angle = get_minAreaRect(circle_img)[-1]
            rotated = rotate_bound(circle_img, angle)
            cv2.imshow("rotate", rotated)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            rotated_gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
            cv2.imshow("rotated_gray", rotated_gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            ret, binary = cv2.threshold(rotated_gray, 100, 255, cv2.THRESH_BINARY)
            cv2.imshow("binary", binary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(rotated, contours[0], -1, (0, 255, 0), 1)
            cv2.imshow("rotate", rotated)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            if len(contours) == 0:
                number = 1
            else:
                x_1, y_1, w_1, h_1 = cv2.boundingRect(contours[0])
                cv2.rectangle(rotated, (x_1, y_1), (x_1+w_1, y_1+h_1), (0, 255, 0), 1)
                cv2.imshow("rotated", rotated)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_nu = binary[y_1 - padding:y_1+h_1 + padding, x_1 - padding:x_1+w_1 + padding]
                cv2.imshow("img_nu", img_nu)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                roismall = cv2.resize(img_nu, (resize_img_y, resize_img_x), interpolation=cv2.INTER_CUBIC)
                roismall = roismall.reshape((1, resize_img_y*resize_img_x))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k=1)
                number = int((results[0][0]))
            print("the number is:", number)
            text = "x:" + str(x) + " y:" + str(y) + "\nR:" + str(r) + "\nnumber:" + str(number)
            # 在原图用指定颜色标记出圆的位置
            img = cv2.circle(img, (x, y), r, (0, 255, 0), 2)
            for i, text in enumerate(text.split('\n')):
                y1 = y + i * 25
                cv2.putText(img, text, (x, y1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), 2)

        # 显示新图像
        cv2.imshow('res', img)

        # # 按esc键退出
        # if cv2.waitKey(0) == 27:
        #     sys.exit()
        #     # cv2.destroyAllWindows()

# -----------------------------------------------------
# 载入并显示图片
padding = 0
resize_img_y = 56  # resize training sample
resize_img_x = 56

# # #  ****读图********
# # # img = cv2.imread('circle2.png')
# # # img = cv2.imread('112.png')
# # # img = cv2.imread('233.png')

img = cv2.imread('./data/1.png')
# img = cv2.imread('4444.jpg')
# img = cv2.imread('no.png')

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
detecte_circle(img)


# # # # ******** 摄像头获取图片************
# videoCaputer = cv2.VideoCapture(1)
# # # videoCaputer.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1920
# # # videoCaputer.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 1080
# #
# while True:
#     _, frame = videoCaputer.read()
#     print(frame.shape)
#     cv2.imshow("test", frame)
#     if cv2.waitKey(1) == 27:
#         break
#     detecte_circle(frame)
# videoCaputer.release()
# cv2.destroyAllWindows()



