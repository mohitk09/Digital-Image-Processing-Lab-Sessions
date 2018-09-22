import matplotlib.pyplot as plt
from skimage import io


def Equalize(img):
    Image_obj_count = img
    plt.subplot(2, 2, 1)
    plt.hist(Image_obj_count.ravel(), 256, [0, 256])
    plt.subplot(2,2,3)
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    pdf = [0 for i in range(0, 256)]
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            pdf[int(img[i][j])] += 1
    print(pdf)
    cdf = [0 for i in range(0,256)]
    sum = 0
    for i in range(0,256):
        sum += pdf[i]
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
    return [img, Image_obj_count,new_grey_levels]
    # img is the modified image and Image_obj_count original image


img_test = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Lena.tiff', as_gray=True)
img_test *= 255
img_input_2, img_input_1, new_grey_levels_input = Equalize(img_test)
# for the specified histogram
img_test = io.imread('D:\\Study material\\7th sem\\DIP\\Test_Images\\Pepper.tiff', as_gray=True)
img_test *= 255
img_specified_2,img_specified_1, new_grey_levels_specified = Equalize(img_test)
#final_image = [[0 for i in range(0, len(img_input_1[0]))] for j in range(0, len(img_input_1))]
plt.subplot(1,2,1)
plt.hist(img_input_2.ravel(), 256, [0, 256])
for i in range(0,255):
    min = 500
    index = 0
    for j in range(0,255):
        if abs(new_grey_levels_specified[j]-new_grey_levels_input[i])<min:
            min = abs(new_grey_levels_specified[j]-new_grey_levels_input[i])
            index = j
    img_input_2[i][j] = new_grey_levels_specified[index]
# for mapping the values
'''
final_image = [[0 for i in range(0, len(img_input_1[0]))] for j in range(0, len(img_input_1))]
for i in range(0,len(img_input_2)):
    for j in range(0,len(img_input_2[i])):
        min = 500
        index_i = 0
        index_j = 0
        for p in range(0,len(img_specified_2)):
            for q in range(0,len(img_specified_2[p])):
                if img_input_2[i][j]-img_specified_2[p][q]<min and img_input_2[i][j]-img_specified_2[p][q]>=0:
                    min = img_input_2[i][j]-img_specified_2[p][q]
                    index_i = p
                    index_j = q
        final_image[i][j]  = img_specified_1[index_i][index_j]
'''

plt.subplot(1,2,2)
plt.hist(img_input_2.ravel(), 256, [0, 256])
plt.show()