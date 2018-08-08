from skimage import util
from skimage.transform import rotate
import matplotlib.pyplot as plt
import numpy as np


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

img = plt.imread('golds.jpg')
gray = rgb2gray(img)
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()

inv = util.invert(gray)
plt.imshow(inv, cmap=plt.get_cmap('gray'))
plt.show()

new_pic = rotate(gray, 180)
plt.imshow(new_pic, cmap=plt.get_cmap('gray'))
plt.show()
