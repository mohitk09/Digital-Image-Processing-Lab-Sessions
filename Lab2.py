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

'''

img = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Lena.tiff', as_gray=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
img = img*255

img = converting_int(img)
print(img)

plt.show()
plt.subplot(2,2,1)
'''


def reduce_pixels(img):
    new_img = []
    for i in range(0,len(img)):
        if(i%2==0):
            temp = []
            for j in range(0,len(img[i])):
                if j%2==0:
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

    img /= 2
    img = converting_int(img)
    plt.axis('off')
    plt.subplot(2, 4, 8)
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.axis('off')
    plt.show()

'''
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

intensity_resolution(img)
'''

# counting the number of objects
Image_obj_count = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\TestIMage.png', as_gray=True)
print(len(Image_obj_count),len(Image_obj_count[0]))
# plt.imshow(Image_obj_count, cmap=plt.get_cmap('gray'))
Image_obj_count = Image_obj_count*255
plt.hist(Image_obj_count.ravel(), 256, [0, 256])
plt.show()


def count_objects(img):
    objects = [[0 for i in range(0,len(img[0]))] for j in range(0,len(img))]
    object_count = 1
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            flag = 0
            if i == 0:
                objects[i][j] = 1
                flag = 1
            else:
                if img[i][j] <= img[i-1][j]+10 and img[i][j]+10 >= img[i-1][j]:
                    objects[i][j] = objects[i - 1][j]
                    flag = 1
                elif j != 0 and img[i][j] <= img[i-1][j-1]+10 and img[i][j]+10 >= img[i-1][j-1]:
                    objects[i][j] = objects[i - 1][j-1]
                    flag = 1
                elif j != 0 and img[i][j] <= img[i][j-1]+10 and img[i][j]+10 >= img[i][j-1]:
                    objects[i][j] = objects[i][j-1]
                    flag = 1
                elif j != len(img[i])-1 and img[i][j] <= img[i-1][j+1]+10 and img[i][j]+10 >= img[i-1][j+1]:
                    objects[i][j] = objects[i -1][j+1]
                    flag = 1
            if flag == 0:
                object_count += 1
                objects[i][j] = object_count

    for i in range(len(img)-1, -1, -1):
        for j in range(len(img[i])-1, -1, -1):
            if i != len(img)-1 and j != 0 and img[i][j] <= img[i+1][j-1]+10 and img[i][j]+10 >= img[i+1][j-1]:
                objects[i][j] = objects[i+1][j-1]
            elif i != len(img)-1 and img[i][j] <= img[i+1][j]+10 and img[i][j]+10 >= img[i+1][j]:
                objects[i][j] = objects[i+1][j]
            elif j != len(img[i])-1 and i!=len(img)-1 and img[i][j] <= img[i+1][j+1]+10 and img[i][j]+10 >= img[i+1][j+1]:
                objects[i][j] = objects[i+1][j+1]
            elif j != len(img[i])-1 and img[i][j] <= img[i][j+1]+10 and img[i][j]+10 >= img[i][j+1]:
                objects[i][j] = objects[i][j+1]
    print(objects)
    b = []
    for i in range(0,len(objects)):
        for j in range(0,len(objects[i])):
            if objects[i][j] not in b:
                b.append(objects[i][j])
    print(len(b))

count_objects(Image_obj_count)

