# -*- coding: utf-8 -*-
import torch
import cv2
from PIL import Image
import numpy as np
from skimage import io, transform
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

'''
PyTorch在做一般的深度学习图像处理任务时，先使用dataset类和dataloader类读入图片，在读入的时候需要做transform变换，
其中transform一般都需要ToTensor()操作，将dataset类中__getitem__()方法内读入的PIL或CV的图像数据转换为torch.FloatTensor。
参考：https://oldpan.me/archives/pytorch-transforms-opencv-scikit-image
'''

'''
######
PIL(RGB)数据格式   W*H  
######
'''
img_PIL = Image.open('11.jpg')
# image.show()
print("type of img_PIL:", type(img_PIL),
      "\nsize of img_PIL:", img_PIL.size,
      "\nmode of img_PIL:", img_PIL.mode,
      "\npixel of img_PIL(0，0):", img_PIL.getpixel((0, 0)))
'''
resize w*h
'''
image = img_PIL.resize((500, 400), Image.NEAREST)
# image.show()
print("size of img_PIL_resize:", image.size)

im = np.array(image, dtype=np.float32)  # image = np.array(image)默认是uint8
print("shape of im(numpy):", im.shape)  # H*W*C
'''
神奇的事情发生了，w和h换了，变成(h,w,c)了
注意ndarray中是 行row x 列col x 维度dim 所以行数是高，列数是宽
'''


'''
CV(BGR)数据格式   H*W*C
'''
img_opencv = cv2.imread('11.jpg')
print("========================",
      "\ntype of img_opencv:", type(img_opencv),
      "\nmode of img_opencv:", img_opencv.dtype,
      "\nshape of img_opencv:", img_opencv.shape)

cv2.imshow("10", img_opencv)
img_opencv[400, 100] = [255, 255, 255]
cv2.imshow("11", img_opencv)
cv2.waitKey()

# resize w*h
image = cv2.resize(img_opencv, (500, 400), interpolation=cv2.INTER_LINEAR)
print("shape of image:", image.shape)


'''
skimage 
'''
img_skimage = io.imread('gg.jpg')
print("========skimage ============",
      "\ntype of img_skimage:", type(img_skimage),
      "\nmode of img_skimage:", img_skimage.dtype,
      "\nshape of img_skimage:", img_skimage.shape)


# 定义一个图像显示函数
def my_imshow(image, title=None):
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # 这里延时一下，否则图像无法加载

# plt.figure()
# my_imshow(img_skimage, title='img_skimage')
# # 可以看到opencv读取的图像打印出来的颜色明显与其他不同
# plt.figure()
# my_imshow(img_opencv, title='img_opencv')
# plt.figure()
# my_imshow(img_PIL, title='img_PIL')
#
# # opencv读出的图像颜色通道为BGR，需要对此进行转换
# img_opencv_RGB = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2RGB)
# plt.figure()
# my_imshow(img_opencv_RGB, title='img_opencv_RGB')

'''
to_tensor()函数看到，函数接受PIL Image或numpy.ndarray，将其先由HWC转置为CHW格式，再转为float后每个像素除以255
'''

# ###### transform变换 ###############
# 尺寸变化、缩放
transform_scale = transforms.Compose([transforms.Resize(128)])
temp = transform_scale(img_PIL)
plt.figure()
my_imshow(temp, title='after_scale_PIL')
print("==========after_scale_PIL========",
      "type of img_PIL_tr:", type(temp),
      "\nsize of img_PIL_tr:", temp.size,
      "\nmode of img_PIL_tr:", temp.mode,
      "\npixel of img_PIL_tr(0，0):", temp.getpixel((0, 0)))


'''
# 随机裁剪
transform_randomCrop = transforms.Compose([transforms.RandomCrop(32, padding=4)])
temp = transform_scale(img_PIL)
plt.figure()
my_imshow(temp, title='after_randomcrop')

# 随机进行水平翻转（0.5几率）
transform_ranHorFlip = transforms.Compose([transforms.RandomHorizontalFlip()])
temp = transform_scale(img_PIL)
plt.figure()
my_imshow(temp, title='after_ranhorflip')

# 随机裁剪到特定大小
transform_ranSizeCrop = transforms.Compose([transforms.RandomSizedCrop(128)])
temp = transform_ranSizeCrop(img_PIL)
plt.figure()
my_imshow(temp, title='after_ranSizeCrop')

# 中心裁剪
transform_centerCrop = transforms.Compose([transforms.CenterCrop(128)])
temp = transform_centerCrop(img_PIL)
plt.figure()
my_imshow(temp, title='after_centerCrop')

# 空白填充
transform_pad = transforms.Compose([transforms.Pad(4)])
temp = transform_pad(img_PIL)
plt.figure()
my_imshow(temp, title='after_padding')
'''


'''
PIL与Tensor转换
将其先由HWC转置为NCHW格式，再转为float后每个像素除以255.
https://blog.csdn.net/qq_36022260/article/details/88907374
'''
loader = transforms.Compose([
      transforms.ToTensor()
])

unloader = transforms.ToPILImage()

#   PIL2tensor
image_PIL2tensor = loader(img_PIL).unsqueeze(0)
print(
      "size of image_tensor", image_PIL2tensor.size(),
      "\npixel of image_tensor", image_PIL2tensor[0, :, 0, 0]
)


# tensor2PIL
def tensor_to_PIL(tensor):
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unloader(image)
    return image


'''
cv格式（numpy）与 tensor转换
https://blog.csdn.net/qq_36022260/article/details/88907374
'''

# numpy2tensor
'''
def toTensor(img):
    assert type(img) == np.ndarray,'the img type is {}, but ndarry expected'.format(type(img))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.from_numpy(img.transpose((2, 0, 1)))
    return img.float().div(255).unsqueeze(0)
'''
image_cv2tensor = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2RGB) # opencv读出的格式为bgr格式
# numpy中transpose(2, 0, 1)将cv的图像维度HWC转换为CHW -> float() tensor转换为float类型 -> div(255) 除以255归一化
# -> unsqueeze(0) 将CHW转变为NCHW (N为1)
image_cv2tensor = torch.from_numpy(image_cv2tensor.transpose(2, 0, 1)).float().div(255).unsqueeze(0)
print(
      "size of image_cv2tensor", image_cv2tensor.size(),
      "\npixel of image_cv2tensor", image_cv2tensor[0, :, 0, 0]
)

# tensor2numpy


def tensor_to_np(tensor):
    img = tensor.mul(255).byte()
    img = img.cpu().numpy().squeeze(0).transpose((1, 2, 0))
    return img

