import numpy as np
import cv2

from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = cv2.imread('../testData/liudehua.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img',img)

image = Image.open('../testData/liudehua.jpg')
print(image.format,image.size,image.mode)
image.show()

image1 = imread('../testData/liudehua.jpg')  # 读入图像(设定合适的路径!) plt.imshow(img)
plt.imshow(image1)
plt.show()






