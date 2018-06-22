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
with open('/Users/kitreatakataglushkoff/Documents/All_Documents/SUMMER_2018/Glaciology/HiMAT/KitSample/Sampleglacier1_mb_bins.csv', 'r') as csvinput:
    plots = csv.reader(csvinput, delimiter = ',')
    #set it so it only appends starting on the second row
    plots = list(plots)
    for row in plots[1:]:
        x.append(float(row[0])) #sets elevations as x values
        y.append(float(row[7])) #sets dh/dt med as y values
        


import numpy as np

#x, y = np.loadtxt('Sampleglacier1_mb_bins.csv', delimiter = ',', unpack = True)


#x2 = []  #define where to pull the x2 values from
#y2 = []  #define where to pull the y2 values from

plt.plot(x, y, label = 'First Line based on File') #
#plt.plot(x2, y2, label = 'Second Line') #plots the line, and an associated label
plt.xlabel('X Axis Plot Number')
plt.ylabel('Y Axis Variable')
plt.title('My Cool Graph\nSee!')
plt.legend() #shows the plot legends
plt.show() #reveals the plot

