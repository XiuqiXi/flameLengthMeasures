# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:23:12 2020

@author: xixiu
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# # subfolder name
# folder_name = './S5C3_JPEG'
# # first frame name
# first_name = '1589278821971-S5C3.jpeg'

# file_name = folder_name + first_name

def flame_length_measure(img, threshold):
    img = cv.imread(img)
    
    img = img[:, 24:561, :]
    
    # img_cropped = img[408:808, :, :]
    
    img_cropped = img
    
    
    [b, g, r] = cv.split(img_cropped)
    # img_theshold = b/255.0
    # # img_theshold = cv.cvtColor(img_cropped, cv.COLOR_BGR2GRAY)
    # # img_theshold = img_theshold/255
    # gamma = 1
    # img_theshold=np.power(img_theshold,gamma)
    img_theshold = b
    T, img_theshold = cv.threshold(b, threshold, 1, cv.THRESH_BINARY)

    
    # edges = cv.Canny(img_theshold,30,200)
    
    sum_all_pixels = np.sum(img_theshold)
    
    # sum_all_pixels = img_theshold.shape[0]*img_theshold.shape[1]*255-sum_all_pixels
    
    k = sum_all_pixels/img_theshold.shape[0]

    # contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # cnt = contours[0]
    # #img_coutours = cv.drawContours(img_gray, [cnt], 0, (0, 255, 0), 3)
    
    # leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    # return_value = leftmost[0]
    # rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    
    # img2 = img_cropped.copy()
    # cv.circle(img2, leftmost, 5, (0, 255, 255), -1)
    # cv.circle(img2, rightmost, 5, (0, 255, 255), -1)
    
    
    flame_length = plt.Figure(figsize=(1, 1), dpi=100)
    axs = flame_length.add_subplot(111)
    axs.imshow(b)
    axs.axvline(x=k, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    # time.sleep(2)

    
    # flame_length = []
    # flame_length.append(leftmost[0])
    
    k = k*0.332103321
    
   
    return k, flame_length
    #1589279017853
    #1589278877211
    #1589278977177
    #1589278734340
    
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
k, flame_length_figure = flame_length_measure('1589278643396-S5C3.jpeg', 50)
root=tkinter.Tk()       #实例化一个窗体对象
root.wm_title('hello,python')     #设置该窗体的标题为hello,python
root.geometry('1500x900')          #设置窗体大小为宽300，高200，中间用键盘上的x表示

# #在窗体root上添加label标签
# label=tkinter.Label(root)   
# label['text']='welcome to the first GUI program using python!'
# label['font']=14    #标签字体大小
# label['fg']='red'    #标签文本颜色为红色
# label.pack()        #标签pack方法布局

# def callback():     #定义回调函数，当点击按钮时，设置标签对象的文本颜色为蓝色
#     label['fg']='blue'  #将label标签对象的文本设置为蓝色
#     k = flame_length_measure('1589278643396-S5C3.jpeg')
    
# def callback_for_scale():
#     print
    
# btn=tkinter.Button(root)        #在root窗体上绘制一个Button按钮对象
# btn['text']='点击我，标签字体颜色将变成蓝色哦'     #按钮上的文本内容
# btn['font']=14          #设置文本大小为14号字体
# btn['fg']='white'       #设置fg属性，按钮文本颜色为白色
# btn['bg']='blue'        #设置bg属性，按钮背景颜色为蓝色
# btn['command']=callback #定义点击按钮时响应事件为callback函数
# btn.pack()              #设置按钮对象在窗体上的位置

# v = tkinter.StringVar()
# s1 = tkinter.Scale(root,from_ = 0,to = 42)
# s1.pack()
# s2 = tkinter.Scale(root,
#       from_ = 0,#设置最小值
#       to = 200,#设置最大值
#       orient = 'horizontal',#设置横向
#       resolution=5,#设置步长
#       tickinterval = 10,#设置刻度
#       length = 600,# 设置像素
#       variable = v)#绑定变量
# s2.pack()
# print(v.get())
# def show():
#     print(s1.get(),s2.get())
# tkinter.Button(root,text = '获取位置',command = show).pack()#用command回调函数获取位置

v = tkinter.StringVar()
s2 = tkinter.Scale(root,
      from_ = 2,#设置最小值
      to = 75,#设置最大值
      orient = 'horizontal',#设置横向
      resolution=0.1,#设置步长
      tickinterval = 10,#设置刻度
      length = 600,# 设置像素
      variable = v)#绑定变量
s2.pack()
# flame_length_figure = flame_length_measure('1589278643396-S5C3.jpeg', float(v.get()))
a = v.get()

def drawPic():
    k, flame_length_figure = flame_length_measure('1589278643396-S5C3.jpeg', float(s2.get()))
    drawPic.f.clf()
    drawPic.a = drawPic.f.add_subplot(111)
    canvas = FigureCanvasTkAgg(flame_length_figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    print(float(s2.get()))
    print(k)

drawPic.f = plt.Figure(figsize=(5, 4), dpi=100)
drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
drawPic.canvas.draw()
tkinter.Button(root,text = '获取位置',command = drawPic).pack()#用command回调函数获取位置
# drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)

# canvas = FigureCanvasTkAgg(flame_length_figure, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack()


root.mainloop()         #窗体对象运行,消息循环