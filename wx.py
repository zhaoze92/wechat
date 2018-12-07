#!/usr/bin/env python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import itchat
import math
import PIL.Image as Image
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# 枚举好友，保存图像
pathSaveBase = "/home/zhaoze/my-projects/杂/weixin_avatar/"

def getFriendsPicture():
    pathSave = pathSaveBase + "photo/"
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]
    user = friends[0]["UserName"]
    num = 0

    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        fileImage = open(pathSave + str(num) + ".jpg",'wb')
        fileImage.write(img)
        fileImage.close()
        num += 1

    ls = os.listdir(pathSave)
    each_size = int(math.sqrt(float(640*640)/len(ls)))
    lines = int(640/each_size)
    image = Image.new('RGBA', (640, 640))
    x = 0
    y = 0

    for i in range(0,len(ls)+1):
        try:
            img = Image.open(pathSave + str(i) + ".jpg")
        except IOError:
            print("Error")
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    image.save(pathSave + 'all.jpg')
    itchat.send_image(pathSave + "all.jpg", "filehelper")

def pictureExcu():
    img1 =np.array(Image.open('/home/zhaoze/my-projects/杂/weixin_avatar/0.jpg')) # 640*640*3
    img2 =np.array(Image.open('/home/zhaoze/my-projects/杂/weixin_avatar/1.jpg'))

    rows, cols, rng = img1.shape

    # 按照4:1进行照片处理
    for i in range(rows):
        for j in range(cols):
            for k in range(rng):
                img2[i,j,k] = (img1[i,j,k]+img2[i,j,k]*4)/5

    io.imsave(pathSaveBase + 'res.jpg',img2)



    # plt.figure("lena")
    # plt.imshow(img2,cmap='gray')
    # plt.axis('off')
    # plt.show()

    print("done")




if __name__ == "__main__":
    pictureExcu()