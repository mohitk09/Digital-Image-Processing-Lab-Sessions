#Mohit Khotani,CSE-2,2015

import matplotlib.pyplot as plt
from skimage import io
from PIL import Image
import numpy as np

img = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Lena.tiff', as_gray=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
plt.subplot(2,2,1)
def reduce_pixels(img):
    new_img = []
    for i in range(0,len(img)):
        if(i%2==0):
            temp = []
            for j in range(0,len(img[i])):
                if(j%2==0):
                    temp.append(img[i][j])
            new_img.append(temp)
    return new_img



new_image = reduce_pixels(img)
plt.imshow(new_image,cmap=plt.get_cmap('gray'))
plt.subplot(2,2,2)


new_image1 = reduce_pixels(new_image)
plt.imshow(new_image1,cmap=plt.get_cmap('gray'))
plt.subplot(2,2,3)



new_image2 = reduce_pixels(new_image1)
plt.imshow(new_image2,cmap=plt.get_cmap('gray'))
plt.savefig('reduced_image.png')
plt.show()




