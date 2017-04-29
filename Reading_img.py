# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 04:30:02 2016

@author: Adeel
"""



import numpy, scipy.io
from PIL import Image



import numpy as np
import cv2
###################################################################
###################################################################
mypath = 'C:\\Users\\Adeel\\Desktop\\Fungus\\CheckN\\File.jpg'
#train_x=[]
#train_y=[]
#listing = os.listdir(mypath)
#images = numpy.zeros(len(listing), dtype = 'uint8')
#for filename in os.listdir(mypath):
    #print (filename)
#      im = Image.open(open(mypath + filename)) #reads (76,76l
im =  cv2.imread(mypath) #reads (76,76,3)
img = np.asarray(im, dtype='float64') / 256. 

print img
#numpy.savetxt('yourfile.mat',img)

scipy.io.savemat('arrdata.mat', mdict={'arr': img})

#Got normalized by 256 for each channel
#      adeel = img.flatten()
      #adeel = im.flatten()
     # rao = img.reshape(3,76,76).transpose(1,2,0) #to retrieve back the image file not from train_x but from IMG
#train_x.append(img)
     
      
      
