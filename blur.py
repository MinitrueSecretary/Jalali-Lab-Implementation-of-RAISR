
import numpy as np
import os
import cv2
import pickle
import time
from math import floor
from Functions import *

infolder = 'set 14'
outfolder = 'set 14 blur'

# get images from folder
filelist = make_dataset(infolder)
# blur the images and save them in the outfolder
for image in filelist:
    print('\r', end='')
    print('' * 60, end='')
    print('\r Processing ' + image)
    im_uint8 = cv2.imread(image)
    # blur the image
    im_blur = cv2.GaussianBlur(im_uint8,(5,5),0)
    # save the image
    cv2.imwrite(outfolder + '/' + os.path.basename(image), im_blur)
