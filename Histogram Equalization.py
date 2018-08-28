import matplotlib.pyplot as plt
from skimage import io

img = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Lena.tiff', as_gray=True)
Image_obj_count = img*255
img *= 255
plt.subplot(2,2,1)
plt.hist(Image_obj_count.ravel(), 256, [0, 256])
plt.subplot(2,2,3)
plt.imshow(img, cmap=plt.get_cmap('gray'))

#plt.show()
pdf = [0 for i in range(0,256)]
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        pdf[int(img[i][j])] += 1
print(pdf)

cdf = [0 for i in range(0,256)]
sum = 0
for i in range(0,256):
    sum = sum+pdf[i]
    cdf[i] = sum+pdf[i]
print(cdf[255])

probability_cdf = [0 for i in range(0,256)]
for i in range(0,256):
    probability_cdf[i] = cdf[i]/cdf[255]

new_grey_levels = [0 for i in range(0,256)]
for i in range(0,256):
    new_grey_levels[i] = probability_cdf[i]*255
    new_grey_levels[i] = int(new_grey_levels[i])
print(new_grey_levels)


for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        img[i][j] = new_grey_levels[int(img[i][j])]

plt.subplot(2,2,2)
plt.hist(img.ravel(), 256, [0, 256])


plt.subplot(2,2,4)
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()

