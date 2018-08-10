#Mohit Khotani,CSE-2,2015

import matplotlib.pyplot as plt
from skimage import io
import matplotlib.image as mp
from PIL import Image
import numpy as np

def converting_int(img):
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            img[i][j] = int(img[i][j])
    return img


img = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Lena.tiff', as_gray=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
img = img*255

img = converting_int(img)
print(img)

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
def intensity_resolution(img):
    # for image 1

    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 1)
    plt.imshow(img, cmap=plt.get_cmap('gray'))

    img = img/2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2,4,2)
    plt.imshow(img, cmap=plt.get_cmap('gray'))

    img = img / 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 3)
    plt.imshow(img, cmap=plt.get_cmap('gray'))

    img = img / 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 4)
    plt.imshow(img, cmap=plt.get_cmap('gray'))



    img = img / 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 5)
    plt.imshow(img, cmap=plt.get_cmap('gray'))



    img = img / 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 6)
    plt.imshow(img, cmap=plt.get_cmap('gray'))



    img = img / 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 7)
    plt.imshow(img, cmap=plt.get_cmap('gray'))


    img = img / 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 8)
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.axis('off')
    plt.show()


def separate(img):
    for i in range(0,len(img)):
        if i!=0 and i!=len(img)-1:
            for j in range(0,len(img[i])):
                if(j!=0 and j!=len(img)-1):
                    print()


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


'''

Image_obj_count = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\TestIMage.png', as_gray=True)
plt.imshow(Image_obj_count, cmap=plt.get_cmap('gray'))
#print(Image_obj_count)
temp = []
for i in range(0,len(Image_obj_count)):
    for j in range(0,len(Image_obj_count[i])):
        if Image_obj_count[i][j] not in temp:
            temp.append(Image_obj_count[i][j])
no_of_colors=0
no_of_colors = int(Image_obj_count.max())
print(no_of_colors*255)
plt.hist(Image_obj_count.ravel(),255,[0,255])
plt.show()
#separate(Image_obj_count)

'''
intensity_resolution(img)