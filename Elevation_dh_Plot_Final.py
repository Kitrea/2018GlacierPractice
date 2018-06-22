#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:56:06 2018

@author: kitreatakataglushkoff

Reads csv files, and returns plots of each glacier's dh/dt relative to
 elevation.
"""


import matplotlib.pyplot as plt 
import csv
#import glob
#import errno

infile = 'Sampleglacier1_mb_bins.csv' #user defines input csv file name
x = []
y = []
elev_col_num = 0 #user inputs the col number corresponding to elevation values
dhdt_col_num = 7 #user inputs the column number corresponding to dh/dt values
"""This requires a human to check which column is necessary. If it differs
from file to file, then the program should be able to ID what string it wants
to recognize for the column to pull data from (using index)"""

#note, if file not in same folder as program, define full directory path
with open(infile, 'r') as csvinput:  
    plots = csv.reader(csvinput, delimiter = ',')
    #set it so it  starting on the second row
    data = list(plots)
    #(I could also add here an if statement to ID which column to take)
    for row in data[1:]:
        x.append(float(row[elev_col_num])) #sets elevations as x values
        y.append(float(row[dhdt_col_num])) #sets dh/dt med as y values


plt.plot(x, y, label = 'Sampleglacier1') #
#plt.plot(x2, y2, label = 'Second Line') #plots the line, and an associated label
plt.xlabel('Elevation (m)')
plt.ylabel('dh/dt ')
plt.title('Glacier Height Change Across Elevation')
plt.legend() #shows the plot legends
plt.show() #reveals the plot

