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
    if len(actual_list) < 8:
        for i in range(0, 8-len(actual_list)):
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
    for i in range(0, len(s)):
        val = decimal_to_binary(ord(s[i]))
        list_of_characters.append(val)
    print(list_of_characters)

    if width*height >= (size*8)/bits:
        # here m and n are used to iterate the list of characters and for image iteration i and j are used
        i = 0
        j = 0
        num_of_pixels_used = 0 # can also be calculated by size of the text file and number of bit level of an image used
        count = 0
        val = decimal_to_binary(int(img[i][j]))
        for m in range(0, len(list_of_characters)):
            for n in range(0, len(list_of_characters[m])):
                val[len(val)-1-count] = list_of_characters[m][n]
                count += 1
                if count == bits:
                    num_of_pixels_used += 1
                    img[i][j] = binary_to_decimal(val)
                    if j < len(img[i])-1:
                        j += 1
                    else:
                        j = 0
                        i += 1
                    val = decimal_to_binary(int(img[i][j]))
                    count = 0
        plt.imshow(img, cmap=plt.get_cmap('gray'))
        plt.show()
        retrieve_text(img,bits,num_of_pixels_used,i)
        print(num_of_pixels_used)
    else:
        print("File is too big")


def retrieve_text(img, bits, number_of_pixels_used, rows):
    max_pixels = 0
    list_of_characters = []
    l = []
    for i in range(0, rows+1):
        for j in range(0, len(img[i])):
            val = decimal_to_binary(int(img[i][j]))
            if max_pixels <= number_of_pixels_used:
                for k in range(0, bits):
                    if len(l) < 8:
                        l.append(val[len(val)-1-k])
                    elif len(l) == 8:
                        list_of_characters.append(l)
                        l = []
                        l.append(val[len(val)-1-k])
                max_pixels += 1
            else:
                break
            '''
            if len(l) < 8:
                for k in range(0, bits):
                    l.append(val[len(val) - 1 - k])
                max_pixels += 1
            else:
                list_of_characters.append(l)
                l = []
                max_pixels += 1
                for k in range(0, bits):
                    l.append(val[len(val)-1-k])
            '''
    print("\n")
    s = ''
    for i in range(0, len(list_of_characters)):
        print(list_of_characters[i])
        val = binary_to_decimal(list_of_characters[i])
        s += chr(val)
    print("Retrieved text from the Image is")
    print(s)


img = io.imread('Pepper.tiff', as_gray=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
img *= 255
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        img[i][j] = int(img[i][j])
text_file = open('Text_to_hide.txt', 'r')
hide_text(img, text_file, 8)
text_file.close()

