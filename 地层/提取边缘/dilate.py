# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/26 20:16
"""
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones(shape=(13, 13))
def dilate_bin_image(bin_image, kernel):
    """
    dilate bin image
    Args:
        bin_image: image with 0,1 pixel value
    Returns:
        dilate image
    """
    kernel_size = kernel.shape[0]
    bin_image = np.array(bin_image)
    if (kernel_size%2 == 0) or kernel_size<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    if (bin_image.max() != 1) or (bin_image.min() != 0):
        raise ValueError("input image's pixel value must be 0 or 1")
    d_image = np.zeros(shape=bin_image.shape)
    center_move = int((kernel_size-1)/2)
    for i in range(center_move, bin_image.shape[0]-kernel_size+1):
        for j in range(center_move, bin_image.shape[1]-kernel_size+1):
            d_image[i, j] = np.max(bin_image[i-center_move:i+center_move,j-center_move:j+center_move])
    return d_image
# d_image = dilate_bin_image(bin_image, kernel)
# plot_image = [bin_image, d_image]
# plot_title = ["original image", "dilate image"]
# plt.figure()
# for i in range(1, len(plot_image)+1):
#     plt.subplot(1, len(plot_image), i)
#     plt.imshow(plot_image[i-1], cmap="gray")
#     plt.title(plot_title[i-1])
# plt.show()
