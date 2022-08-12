from skimage.io import imread
from skimage.io import imshow

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def printimages(filelist):
    for i in filelist:
        plt.figure()
        plt.imshow(mpimg.imread(i))
        plt.plot()