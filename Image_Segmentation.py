from skimage import io
import matplotlib.pyplot as plt
import numpy as np
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



