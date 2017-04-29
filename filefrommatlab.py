# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 08:17:37 2016

@author: Adeel
"""

import numpy, scipy.io
from PIL import Image

import os

import glob


from os import listdir

import numpy as np
import cv2
###################################################################
###################################################################
mypath = 'C:\\Users\\Adeel\\Desktop\\Fungus\\CheckN\\'

#mypath = 'C:\\Users\\Adeel\\Desktop\\Fungus\\Check\\lp114.jpg'
#train_x=[]
#train_y=[]


for filename in os.listdir(mypath):
#images = numpy.zeros(len(listing), dtype = 'uint8')
#for filename in os.listdir(mypath):
    #print (filename)
#im = Image.open(open(mypath + listing)) #reads (76,76l
    im =  cv2.imread(mypath + filename ) #reads (76,76,3)
    img = np.asarray(im, dtype='float64') / 256. 
    #train_x.append(img)
print img
#numpy.savetxt('yourfile.mat',img)
#scipy.io.savemat('ab.mat', img)

scipy.io.savemat('ab.mat', mdict={'ab': img})
