import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
from matplotlib.colors import NoNorm
from PIL import ImageEnhance, Image

image = mpimg.imread('im.png')
implot = plt.imshow(image)
plt.show()

arr = image.mean(axis = -1)
plt.imshow(arr, norm = NoNorm(), vmin =30, vmax =200)
plt.show()


image1 = ImageEnhance.Contrast(Image.fromarray(np.uint8(image))).enhance(2.0)
plt.imshow(image1)
plt.show()

i_red, i_blue, i_green = image.copy(), image.copy(), image.copy()
i_red[:,:, 1], i_red[:, :, 2] = 0, 0
plt.imshow(i_red)
plt.show()
i_blue[:, :, 0], i_blue[:, :, 1] = 0, 0
plt.imshow(i_blue)
plt.show()
i_green[:, :, 0], i_green[:, :, 2] = 0, 0
plt.imshow(i_green)
plt.show()




arr = image.mean(axis = -1)
plt.imshow(arr, cmap = plt.get_cmap('gray')) 
plt.show()

