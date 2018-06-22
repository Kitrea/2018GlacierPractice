#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:56:06 2018

@author: kitreatakataglushkoff

Practice with Plots
"""

#import pandas as pd

#import matplotlib

import matplotlib.pyplot as plt 


x = [] #define where to pull the x values from, into a list
y = []  #define where to pull the y values from


import csv


#first, doing it without numpy, as follows:
#if file not in same folder as program, define full directory path
#with open('/Users/kitreatakataglushkoff/Documents/All_Documents/SUMMER_2018/Glaciology/HiMAT/KitSample/Sampleglacier1_mb_bins.csv', 'r') as csvinput:
with open('Sampleglacier1_mb_bins.csv', 'r') as csvinput:  
    plots = csv.reader(csvinput, delimiter = ',')
    #set it so it only appends starting on the second row
    data = list(plots)
    #(I could also add here an if statement to ID which column to take)
    for row in data[1:]:
        x.append(float(row[0])) #sets elevations as x values
        y.append(float(row[7])) #sets dh/dt med as y values
       

"""
#trying with numpy
import numpy as np
import os

data_input = np.genfromtxt('Sampleglacier1_mb_bins.csv', delimiter=',')
plt.plot(data_input[0], data_input[7], color='r', label='the data')
"""
#x2 = []  #define where to pull the x2 values from
#y2 = []  #define where to pull the y2 values from

plt.plot(x, y, label = 'Sampleglacier1') #
#plt.plot(x2, y2, label = 'Second Line') #plots the line, and an associated label
plt.xlabel('Elevation (m)')
plt.ylabel('dh/dt ')
plt.title('Glacier Height Change Across Elevation')
plt.legend() #shows the plot legends
plt.show() #reveals the plot

