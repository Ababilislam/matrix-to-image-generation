#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ababil islam udoy
"""

la = [[1, 1, 1, 1, 1, 1, 1, 0, 0, '01', '00', '00', '11', 0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, '01', '00', '10', '11', 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, '10', '11', '00', '00', 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, '00', '11', '00', '00', 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, '01', '00', '00', '10', 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, '01', '00', '10', '01', 0, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, '10', '11', '11', '00', 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 1, '00', '11', '11', '01', 1, 1, 0, 0, 0, 1, 0, 0], ['00', '11', '00', '00', '01', '00', 0, '00', '00', '01', '11', '01', '01', '10', '00', '01', '10', '10', '01', '01', '01'], ['00', '10', '10', '11', '10', '10', 1, '00', '11', '01', '11', '10', '01', '00', '00', '11', '01', '10', '11', '10', '01'], ['00', '00', '01', '10', '11', '10', 0, '10', '00', '00', '11', '00', '01', '10', '01', '00', '01', '10', '00', '01', '01'], ['00', '00', '11', '10', '01', '10', 1, '00', '11', '00', '01', '10', '01', '11', '11', '11', '01', '00', '00', '10', '01'], [0, 0, 0, 0, 0, 0, 0, 0, 1, '11', '10', '01', '00', '10', '01', '01', '10', '01', '01', '10', '00'], [1, 1, 1, 1, 1, 1, 1, 0, 1, '10', '10', '10', '01', '10', '01', '10', '01', '01', '01', '11', '01'], [1, 0, 0, 0, 0, 0, 1, 0, 1, '11', '11', '00', '11', '10', '00', '11', '00', '10', '01', '11', '01'], [1, 0, 1, 1, 1, 0, 1, 0, 1, '01', '00', '10', '01', '00', '00', '11', '01', '10', '11', '00', '01'], [1, 0, 1, 1, 1, 0, 1, 0, 0, '01', '00', '11', '01', '00', '01', '10', '00', '10', '01', '10', '11'], [1, 0, 1, 1, 1, 0, 1, 0, 1, '11', '01', '10', '01', '10', '00', '11', '01', '01', '10', '01', '00'], [1, 0, 0, 0, 0, 0, 1, 0, 1, '10', '11', '10', '11', '10', '01', '01', '01', '11', '01', '00', '01'], [1, 1, 1, 1, 1, 1, 1, 0, 1, '00', '10', '10', '01', '01', '00', '10', '01', '10', '01', '00', '00']]

import numpy as np
from PIL import Image,ImageOps
import glob
import os

# open images by providing path of images
img1 = Image.open("raw/img1.jpg")
img2 = Image.open("raw/img2.jpg")
img3 = Image.open("raw/img_3.png")
img4 = Image.open("raw/img-4.png")

#++++++++++++++++ gray scelling++++++++++++++++
img1 = ImageOps.grayscale(img1)
img2 = ImageOps.grayscale(img2)
img3 = ImageOps.grayscale(img3)
img4 = ImageOps.grayscale(img4)

# +++++++++++++++image resize++++=
img1 = img1.resize((50, 50))
img2 = img2.resize((50, 50))
img3 = img3.resize((50, 50))
img4 = img4.resize((50, 50))

# ++++++++image displaying +++++++
# img1.show()
# img2.show()
# img3.show()
# img4.show()

# need to convert image in to numpy arrary
img_array_1 = np.array(img1)
img_array_2 = np.array(img2)
img_array_3 = np.array(img3)
img_array_4 = np.array(img4)

z = np.zeros((50,0))
# print(len(la[1])*50+4)
matrixsize=len(la[1])*50
f=np.zeros((4,matrixsize))
# z=[[]]
# print(np.shape(z))
# print(img_array_1)

# x=[[]]         #need to assign numpy dynamic array.

    
x = np.zeros((0,matrixsize))
for i in range(len(la)):
    for j in range(len(la[i])):
        # print(j,end=",")
        val=la[i][j]
        value=int(val)
        # print("value:{}  ,type {}".format(value, type(value)))
        if value==0:
            z=np.append(z, img_array_1, axis=1)
            # z.append(img_array_1)
        elif value==1:
            z=np.append(z, img_array_2, axis=1)
            
        elif value==10:
            z=np.append(z, img_array_3, axis=1)
            
        elif value==11:
            z=np.append(z, img_array_4, axis=1)
    # x.append(z)
    x=np.append(x,z,axis=0)
    # z=[[]]
    z = np.zeros((50,0))
# z.show()

# print(type(x))
# print(np.shape(z))        
# new_x= x.convert('RGB')
# finalImage = Image.fromarray(x)
# finalImage.show()

# print(np.shape(z))

# finalImage.save('generated_image.png')

x=x/255
# for horigontal adjustment of border,
# print(type(x))
s=np.shape(x)
v=s[0]
# print(v)  
tl=np.ones((v,50))                 #white tag tl=left tr=tag right
tr=np.ones((v,50))
hl = np.hstack((tl,x))
hr = np.hstack((hl,tr))
# for vertical adjustment with white border
# print(type(hr))
s=np.shape(hr)
vt=s[1]
# print(vt)
tv=np.ones((50,vt))                  #matrix with one 
vu = np.vstack((tv,hr))
vd = np.vstack((vu,tv))
fr=vd*255
# convert numpy array to image object
finalImage=Image.fromarray(fr)
# to show image 
# finalImage.show()
#
# finalImage.save("4QR.jpeg")

import imageio
imageio.imwrite('4qr.jpeg', finalImage)

