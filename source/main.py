import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image


def show_basic_info(img):
    print("size: {}".format(img.size))
    print("mode: {}".format(img.mode))

def calc_hist(img):
    width, lenth = img.size
    hist = {i: 0 for i in range(256)}
    for x in range(width):
        for y in range(lenth):
            hist[img.getpixel((x,y))] += 1
    return hist

def mat_version(file_name):
    img = mpimg.imread(file_name)
    print(img)
    imgplot = plt.imshow(img)
    lum_img = img[:, :, 0]

    # This is array slicing.  You can read more in the `Numpy tutorial
    # <https://docs.scipy.org/doc/numpy-dev/user/quickstart.html>`_.

    plt.imshow(lum_img)

    # imgplot = plt.imshow(lum_img)
    # plt.colorbar()


def PIL_version(file_name):
    im = Image.open(file_name)
    show_basic_info(im)
    # im.show()
    grey_image = im.convert('L')
    # grey_image.show()
    hist = calc_hist(grey_image)
    print(hist)

if __name__ == "__main__":
    file_name = "test2.jpg"
    mat_version(file_name)
    