#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:11:46 2021

@author: ab
"""

la = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]]

import numpy as np
from PIL import Image,ImageOps
import glob
import os

# open images by providing path of images
img1 = Image.open("1.jpeg")
img2 = Image.open("2.jpeg")

#++++++++++++++++ gray scelling++++++++++++++++
img1 = ImageOps.grayscale(img1)
img2 = ImageOps.grayscale(img2)
# ++++++++++++++++++++++image resize++++=
img1 = img1.resize((50, 50))
img2 = img2.resize((50, 50))
# img1.show()
# img2.show()



# need to convert image in to numpy arrary
img_array_1 = np.array(img1)
img_array_2 = np.array(img2)
z = np.zeros((50,0))
# print(len(la[1])*50+4)
matrixsize=len(la[1])*50+4
f=np.zeros((4,matrixsize))
# z=[[]]
print(np.shape(z))
# print(img_array_1)

x=[[]]         #need to assign numpy dynamic array.

# for i in range(len(la)):
    
#     for j in range(len(la[i])):
#         print(j,end=",")
#         if la[i][j]==0:
#             z=np.append(z, img_array_1, axis=1)
#             # z.append(img_array_1)
#         elif la[i][j]==1:
#             # z=np.insert(z,img_array_2)
#             z=np.append(z, img_array_2, axis=1)
#     print(" ")      
#     # x.append(z)
#     z.show()
#     f=np.append(f,z,axis=0)
    # z=np.clean()

# print(np.delete(x,[0]))
# k=[[]]
# for i in range(1,len(x)):
#     # for j in range(len(z[i])):
#     k=np.append(k,x[i],axis=0)
        



# ab= np.array(x,dtype='int64')
# print(ab.remove(0))
    
x = np.zeros((0,850))
for i in range(len(la)):
    for j in range(len(la[i])):
        print(j,end=",")
        if la[i][j]==0:
            z=np.append(z, img_array_1, axis=1)
            # z.append(img_array_1)
        elif la[i][j]==1:
            z=np.append(z, img_array_2, axis=1)
    # x.append(z)
    x=np.append(x,z,axis=0)
    # z=[[]]
    z = np.zeros((50,0))
# z.show()

# print(type(x))
# print(np.shape(z))        
finalImage = Image.fromarray(x)
finalImage.show()

# print(np.shape(z))

# finalImage.save('collage.png')

"""i cant work with hstack or vstack i need to work with numpy array and add image colloumn wise,"""









# print(h1)
# h1 = np.hstack((h1))

# for i in la:
#     # print(i, end=' ')
#     k = int(i)
#     # print(type(k))
#     # print(k,end=',')
#     if i == 0 or "00":
#         f = 0
#         # h1=np.array(h1)
#         # h1 = np.hstack((h1,img_array_1))
#     # elif i == '01;' or "1" or 1:
#     #     f = 1
#     #     h1 = np.hstack((h1,img_array_2))
#     # elif i == '10' or "10" or 10:
#     #     f = 3
#     #     h1 = np.hstack((h1,img_array_3))
#     # elif i == '11' or "11" or 11:
#     #     f = 4
#     #     h1 = np.hstack((h1,img_array_4))

# # finalImage = Image.fromarray(h1)
# finalImage.show()
# #
# finalImage.save('collage.png')
# # _________________i need to resize image ______________
# print("{}".format(img1.format))
# print("size:{}".format(img1.size))
# print("mode:{}".format(img1.mode))
#
# # +++++++++++++++++++++++ append images in to list+++++++++
# unsize_image_list = []
# image_list = []
# for file_name in glob.glob('*.jpg'):
#     print(file_name)
#     img = Image.open(file_name)
#     unsize_image_list.append(img)
# # print(unsize_image_list)
# # +++++++++++++++Imge resizing++++++++++++
# for image in unsize_image_list:
#     # image.show()
#     image=image.resize((50, 50))
#     image_list.append(image)
#     # image.show()
# # print(image_list)
# # ++++++++save resize image_++++++++++=
# for i, image in enumerate(image_list):
#     image.save('{}{}{}'.format('resize50*50/image', i+1, '.png'))
# # =======================image resizing done====================


# create arrays of above images
# img_array_1 = np.array(img1)
# img_array_2 = np.array(img2)
# img_array_3 = np.array(img3)
# img_array_4 = np.array(img4)
# # print(img1_array)
# # ====== collaging images ======
# h1 = np.hstack((img_array_1, img_array_2, img_array_3, img_array_4))
# h2 = np.hstack((img_array_4, img_array_3, img_array_2,img_array_1))
#
# arrayImageFinal= np.vstack((h1, h2))
#
# finalImage=Image.fromarray(arrayImageFinal)
#
# finalImage.save('collage.png')
