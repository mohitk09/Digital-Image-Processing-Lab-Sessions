from skimage import io
import matplotlib.pyplot as plt
import numpy as np
'''
img = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\test_image.png', as_gray=True)
img = img*255

pixels = [0 for i in range(0,256)]
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        val = int(img[i][j])
        pixels[val] += 1
print(pixels)

max1 = pixels[0]
max2 = pixels[0]
max2_index = 0
min_index = 0
min = pixels[0]
for i in range(0,len(pixels)):
    if max1<pixels[i] and max2 <pixels[i] :
        max1 = pixels[i]
    if max1>pixels[i] and max2<pixels[i]:
        max2 = pixels[i]
        max2_index = i
    if min>pixels[i] and pixels[i]!=0:
        min = pixels[i]
        min_index = i

print(max2)
print(min)
print(max2_index)
print(min_index)
new_image = np.empty([len(img),len(img[0])], dtype=np.uint8)
new_image1 = np.empty([len(img),len(img[0])], dtype=np.uint8)
for i in range(0,len(new_image)):
    for j in range(0,len(new_image[i])):
        new_image[i][j] = 255
        new_image1[i][j]  = 255
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        if int(img[i][j]) == max2_index or int(img[i][j]) == min_index:
            new_image[i][j] = 0
        elif int(img[i][j]) != max2_index and int(img[i][j]) != min_index and int(img[i][j])!=255:
            new_image1[i][j] = 0

plt.subplot(2,1,1)
plt.imshow(new_image, cmap='gray')
plt.subplot(2,1,2)
plt.imshow(new_image1,cmap='gray')
plt.show()
'''
def global_thresholding(test_image1):
    test_image = np.empty([len(test_image1),len(test_image1[0])])
    l = len(test_image)*len(test_image[0])
    total = 0
    for i in range(0,len(test_image)):
        for j in range(0,len(test_image[0])):
            total += test_image1[i][j]
    comparison_value = total/l
    for i in range(0,len(test_image)):
        for j in range(0,len(test_image)):
            if test_image1[i][j]>comparison_value:
                test_image[i][j] = 255
            else:
                test_image[i][j] = 0
    plt.imshow(test_image,cmap='gray')
    plt.show()
    return test_image
def local_thresholding(test_image):
    test_image = np.array(test_image, dtype=np.uint)
    test_imagel = np.empty([len(test_image),len(test_image[0])])
    for i in range(0,len(test_image)):
        for j in range(0,len(test_image[i])):
            if i == 0 and j==0:
                total = (test_image[i][j]+test_image[i+1][j]+test_image[i][j+1]+test_image[i+1][j+1])
                mean = total/4
            elif i==0 and j== len(test_image[0])-1:
                total = (test_image[i][j]+test_image[i+1][j]+test_image[i][j-1]+test_image[i+1][j-1])
                mean = total/4
            elif i == len(test_image)-1 and j == 0:
                total = (test_image[i][j] + test_image[i-1][j] + test_image[i][j+1] + test_image[i-1][j+1])
                mean = total / 4
            elif i == len(test_image)-1 and j == len(test_image[0])-1:
                total = (test_image[i][j] + test_image[i][j-1] + test_image[i-1][j] + test_image[i-1][j-1])
                mean = total / 4
            elif i == 0:
                total = test_image[i][j] + test_image[i][j-1]+test_image[i][j+1]+test_image[i+1][j+1]+test_image[i+1][                          j-1]+test_image[i+1][j]
                mean = total / 6
            elif i == len(test_image)-1:
                total = test_image[i][j] + test_image[i][j-1]+test_image[i][j+1]+test_image[i-1][j+1]+test_image[i-1][                          j-1]+test_image[i-1][j]
                mean = total / 6
            elif j == 0:
                total = test_image[i][j] + test_image[i+1][j]+test_image[i-1][j]+test_image[i][j+1]+test_image[i-1][                          j+1]+test_image[i+1][j+1]
                mean = total / 6
            elif j == len(test_image[0])-1:
                total = test_image[i][j] + test_image[i+1][j]+test_image[i-1][j]+test_image[i][j-1]+test_image[i+1][                          j-1]+test_image[i-1][j-1]
                mean = total / 6
            else:
                total = test_image[i][j] + test_image[i+1][j] + test_image[i-1][j] + test_image[i][j-1]+test_image[i][j+1] +                     test_image[i+1][j+1]+test_image[i+1][j-1]+test_image[i-1][j-1]+test_image[i-1][j+1]
                mean = total / 9
            if test_image[i][j]>mean:
                test_imagel[i][j] = 255
    plt.imshow(test_imagel,cmap='gray')
    plt.show()
    return test_imagel

img = io.imread('D:\\Study material\\7th sem\\DIP\\BinDataset\\BinDataset\\Texture.tiff', as_gray=True)
img *= 255
img1 = global_thresholding(img)
img2 = local_thresholding(img)
plt.subplot(1,2,1)
plt.imshow(img1,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(img2,cmap='gray')
plt.show()