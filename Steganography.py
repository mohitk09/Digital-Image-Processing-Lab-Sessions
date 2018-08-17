import matplotlib.pyplot as plt
from skimage import io
import os


def decimal_to_binary(val):
    l = []
    while val >= 1:
        rem = int(val) % 2
        l.append(rem)
        val = int(val)/2
    actual_list = list(reversed(l))
    if len(actual_list)<8:
        for i in range(0,8-len(actual_list)):
            actual_list.insert(i, 0)
    return actual_list


def binary_to_decimal(val):
    decimal_value = 0
    for i in range(0,len(val)):
        decimal_value += val[i]*pow(2,len(val)-i-1)
    return decimal_value



# here bits refers to the bit number where text will be hidden
def hide_text(img, text_file, bits):
    width = len(img)
    height = len(img[0])
    size = os.path.getsize("Text_to_hide.txt")
    print(size)
    s = ''
    while True:
        c = text_file.read()
        if not c:
            break
        s = s+c
    print(s)
    list_of_characters = []
    for i in range(0,len(s)):
        val = decimal_to_binary(ord(s[i]))
        list_of_characters.append(val)
    print(list_of_characters)

    if width*height >= (size*8)/bits:
        # here m and n are used to iterate the list of characters and for image iteration i and j are used
        i = 0
        j = 0
        for m in range(0,len(list_of_characters)):
            for n in range(0,len(list_of_characters[m]),bits):
                val = decimal_to_binary(int(img[i][j]))
                for v in range(0,bits): # v is for iterating the bits level in an image
                    val[len(val)-1-v] = list_of_characters[m][n+v]
                img[i][j] = binary_to_decimal(val)
                if j<len(img[i])-1:
                    j = j+1
                else:
                    j = 0
                    i = i+1
    else:
        print("File is too big")



img = io.imread('Pepper.tiff', as_gray=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
img *= 255
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        img[i][j] = int(img[i][j])
text_file = open('Text_to_hide.txt', 'r')
hide_text(img, text_file, 1)
text_file.close()
plt.show()
