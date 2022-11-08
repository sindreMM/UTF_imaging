import cv2
import numpy as np
from cv2 import IMREAD_GRAYSCALE
import pyperclip
import easygui


def get_img():
    img_file = easygui.fileopenbox()
    return img_file


def to_img(img_file):
    image = cv2.imread(img_file, flags=IMREAD_GRAYSCALE)
    return image


def show_img(name, img):
    cv2.imshow(name, img)
    while True:
        if cv2.waitKey(0) + 0x00 == ord("q"):
            break


def add_to_clipboard(text):
    pyperclip.copy(text)
    # print("art added to clipboard")


def average_square(image, pos, size):
    pixel_list = []
    for y in range(size): # iterates over a square, and stores every value
        for x in range(size):
            pixel_list.append(image[pos[0] + x][pos[1] + y])

    avg_level = np.average(pixel_list)
    return avg_level


def set_square(image, pos, size, value): # sets a square to a given value
    new_image = image
    cv2.rectangle(new_image, tuple(pos)[::-1], (pos[0] + size, pos[1] + size)[::-1], value, thickness=-1)
    return new_image


def set_value(pixel_img, pos, value):
    pixel_img[pos[0]][pos[1]] = value


def pixelate(img, pixelation):
    pixelated_img = np.zeros((len(img) - len(img)%pixelation, len(img[0]) - len(img[0])%pixelation), np.uint8)
    value_img = np.zeros(((len(img))//pixelation, (len(img[0]))//pixelation), np.uint8) # Not currently used

    for n in range(0, len(img) - len(img)%pixelation, pixelation): # loops over every pixel
        for k in range(0, len(img[0]) - len(img[0])%pixelation, pixelation):
            # gets the average value over a square
            avg = average_square(img, [n, k], pixelation)
            # sets value of all pixels within that square to the average value
            pixelated_img = set_square(pixelated_img, [n, k], pixelation, avg)
            set_value(value_img, [n//pixelation, k//pixelation], avg)
    return pixelated_img


def int_to_char(number):
    convert_number = round(260 - number, -1)
    convert_utf = {0: " ", 10: "¨", 20: "'", 30: "`", 40: "-", 50: ":", 60: "^", 70: "*", 80: ">",
                     90: "+", 100: "=", 110: "!", 120: "\\", 130: "|", 140: "?", 150: "x", 160: "¤",
                     170: "#", 180: "£", 190: "%", 200: "8", 210: "0", 220: "§", 230: "Æ", 240: "&", 250: "@", 260: "Ø"}
    try :
        2*convert_utf[convert_number]
    except KeyError:
        # print(KeyError)
        # print(number)
        pass
    return 2*convert_utf[convert_number]


def to_utf(raw_img, pixelation):
    """
    Creates a string from a picture with a utf-symbol corresponding with the gray scale level
    of each pixel
    """
    utf_string = ""
    for row in raw_img[::pixelation]:
        string_row = map(int_to_char, row[::pixelation])
        utf_string += "".join(string_row) + "\n"
    return utf_string


if __name__ == "__main__":
    im = to_img(get_img())
    show_img("Window", im)
    pixel_img = pixelate(im, 3)
    show_img("Window", pixel_img)
    utf = to_utf(pixel_img, 3)
    add_to_clipboard(utf)









