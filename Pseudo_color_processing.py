import cv2
import matplotlib.pyplot as plt


# Reading the Image as Grayscale
im_gray = cv2.imread("D:\\Study material\\7th sem\\DIP\\Test_Images\\bomb.png",cv2.IMREAD_GRAYSCALE)
plt.subplot(2,3,1)
plt.imshow(im_gray,cmap=plt.get_cmap('gray'))

# applying Jet ColorMap of cv2
im_colorj = cv2.applyColorMap(im_gray,cv2.COLORMAP_JET)
plt.subplot(2,3,2)
plt.imshow(im_colorj)


# applying Autumn ColorMap of cv2
im_colora = cv2.applyColorMap(im_gray,cv2.COLORMAP_AUTUMN)
plt.subplot(2,3,3)
plt.imshow(im_colora)


# applying Bone ColorMap of cv2
im_colorb = cv2.applyColorMap(im_gray,cv2.COLORMAP_RAINBOW)
plt.subplot(2,3,4)
plt.imshow(im_colorb)


# applying Pink ColorMap of cv2
im_colorh = cv2.applyColorMap(im_gray,cv2.COLORMAP_PINK)
plt.subplot(2,3,5)
plt.imshow(im_colorh)


# applying HSV ColorMap of cv2
im_color_hsv = cv2.applyColorMap(im_gray,cv2.COLORMAP_HSV)
plt.subplot(2,3,6)
plt.imshow(im_color_hsv)


# Showing the final output
plt.show()


