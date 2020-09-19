# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:39:00 2020

@author: xixiu
"""

import cv2 as cv
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


# def flame_length_measure(img, threshold):
#     img = cv.imread(img)
    
#     img = img[:, 24:561, :]
     
#     img_cropped = img
        
#     [b, g, r] = cv.split(img_cropped)

#     img_theshold = b
#     T, img_theshold = cv.threshold(b, threshold, 1, cv.THRESH_BINARY)

    
#     sum_all_pixels = np.sum(img_theshold)
    
#     k = sum_all_pixels/img_theshold.shape[0]

#     # flame_length = plt.Figure(figsize=(1, 1), dpi=100)
#     # axs = flame_length.add_subplot(111)
#     # axs.imshow(b)
#     # axs.axvline(x=k, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)

    
    
   
#     return b, k

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Application(tk.Tk):
    
    def __init__(self, img_name, threshold):
        '''初始化'''
        super().__init__() # 有点相当于tk.Tk()
        self.wm_title("Embed matplotlib in tkinter")
        self.createWidgets()
        self.createScale()
        self.__ini_threshold = threshold
        self.__img = img_name
        print(self.__img )
        print(self.__ini_threshold)
        
    def createWidgets(self):
       
        fig=plt.Figure(figsize=(5, 5), dpi=100)
        ax=fig.add_subplot(111)
        canvas=FigureCanvasTkAgg(fig,master=self)
        canvas.get_tk_widget().grid(row=4,column=0)
        canvas.draw()
        
        # print(self.__ini_threshold)
        # print(self.__img)
        
        ax.clear()         # clear axes from previous plot
        figure_blue, flame_length, threshold = self.flame_length_measure('TEMP.jpeg', 2)
        ax.imshow(figure_blue)
        ax.axvline(x=flame_length, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
        canvas.draw()
        
        str_Label = tk.StringVar()
        self.plotbutton=tk.Button(master=self, text="flame length", command=lambda: self.plot(canvas,ax))
        self.plotbutton.grid(row=1,column=0)
        self.plotbutton_changeLabel=tk.Button(master=self, text="flame length", command=lambda: str_Label.set("HEELLOOO FROM STRINGVAR!!!"))
        self.plotbutton.grid(row=2,column=0)
        
        self.label = tk.Label(master = self, textvariable = str_Label) 
        # self.label['font']=14    #标签字体大小
        # self.label['fg']='red'    #标签文本颜色为红色
        self.label.grid(row=3,column=0)       #标签pack方法布局
        
    def createScale(self):
        v = tk.StringVar()
        self.s2 = tk.Scale(self,
        from_ = 2,#设置最小值
        to = 75,#设置最大值
        orient = 'horizontal',#设置横向
        resolution=0.1,#设置步长
        tickinterval = 10,#设置刻度
        length = 600,# 设置像素
        variable = v)#绑定变量
        self.s2.grid(row=0,column=0)
        str_Label = 'The threshold is '+str(v.get())
        
        
    def plot(self,canvas,ax):
        ax.clear()         # clear axes from previous plot
        figure_blue, flame_length, threshold = self.flame_length_measure('500s.jpeg', self.s2.get())
        ax.imshow(figure_blue)
        ax.axvline(x=flame_length, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
        canvas.draw()
        print(flame_length)
        print(threshold)
        
    # def flame_length_measure(self,img, threshold):
    #     img = cv.imread(img)
        
    #     img = img[:, 24:561, :]
         
    #     img_cropped = img
            
    #     [b, g, r] = cv.split(img_cropped)
    
    #     img_theshold = b
    #     T, img_theshold = cv.threshold(b, threshold, 1, cv.THRESH_BINARY)
    
        
    #     sum_all_pixels = np.sum(img_theshold)
        
    #     k = sum_all_pixels/img_theshold.shape[0]
    
    #     return b, k, threshold
    
    def flame_length_measure(self, img, threshold):
        img = cv.imread(img)
        
        img_cropped = img[143:1033, 24:561, :]
    
        
        [b, g, r] = cv.split(img_cropped)
        img_theshold = b
    
        
       
        for k in range(img_theshold.shape[1]-1, 0, -1):
            if (sum(img_theshold[:,k])/img_theshold.shape[0] > threshold):
    
                break
    
        
        k = k
        
        return b, k, threshold
    
    
        

app = Application('1589278643396-S5C3.jpeg', 50)
print(app.createScale())
# entry = tk.Entry(root1, textvariable=v)
# 主消息循环:
app.mainloop()


