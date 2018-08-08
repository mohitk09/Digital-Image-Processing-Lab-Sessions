#Mohit Khotani,CSE-2,2015

import matplotlib.pyplot as plt
from skimage import io
from PIL import Image
import numpy as np

img = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Lena.tiff', as_gray=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


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

total_height = 0
total_width = 0
new_image = reduce_pixels(img)
total_height = total_height+len(new_image)
total_width = total_width+len(new_image[0])
plt.imshow(new_image,cmap=plt.get_cmap('gray'))
plt.xlabel('Width')
plt.ylabel('Height')
plt.savefig('reduced_image_1')

new_image1 = reduce_pixels(new_image)
plt.imshow(new_image1,cmap=plt.get_cmap('gray'))
plt.savefig('reduced_image_2.jpg')

total_height = total_height+len(new_image1)
total_width = total_width+len(new_image1[0])


new_image2 = reduce_pixels(new_image1)
plt.imshow(new_image2,cmap=plt.get_cmap('gray'))


total_height = total_height+len(new_image2)
total_width = total_width+len(new_image2[0])


images = map(Image.open, ['new_image.jpg', 'new_image1.jpg', 'new_image2.jpg'])
new_im = Image.new('RGB', (total_width, total_height))
x_offset = 1
for ima in images:
  new_im.paste(ima, (x_offset,0))
  x_offset += ima.size[0]

new_im.save('test.jpg')

plt.savefig('reduced_image_3.jpg')
plt.show()




