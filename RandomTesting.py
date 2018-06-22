#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:53:30 2018

@author: kitreatakataglushkoff

This is for random testing of functions and modules
"""


"""
import numpy as np
import matplotlib.pyplot as plt

data_in = np.genfromtxt('Sampleglacier1_mb_bins.csv', delimiter = ',')
data_in[0:1]
"""

import matplotlib.pyplot as plt 
import csv
import glob

#/Users/kitreatakataglushkoff/Documents/All_Documents/SUMMER_2018/Glaciology/HiMAT/KitSample

#/Users/kitreatakataglushkoff/Documents/All_Documents/SUMMER_2018/Glaciology/HiMAT/DEMs/mb_bins_sample_20180323
infile_path = '/Users/kitreatakataglushkoff/Documents/All_Documents/SUMMER_2018/Glaciology/HiMAT/DEMs/mb_bins_sample_20180323'
region = str(15) #define the region of interest

#identify the directory to pull files from
region_files = glob.glob(infile_path+'/' + region + '*.csv')


elev_col_num = 0 #user inputs the col number corresponding to elevation values
dhdt_col_num = 7 #user inputs the column number corresponding to dh/dt values



"""how to make each next set of x values be stored in a new list? Also, how to 
pull just the name from the string? """
#Loop through each csv file of the given region
for in_file in region_files:
    x = []
    y = []
    #make an empty list, for the set of x values
    #pull the name of the glacier from file title, store as a var
    nameindex = in_file.find(region)
    newname = in_file.replace(in_file[0:nameindex],'')
    glaciername = newname.replace('_mb_bins.csv','')
 
    #read the file
    with open(in_file, 'r') as csvinput:  
        plots = csv.reader(csvinput, delimiter = ',')
        #set it so it  starting on the second row
        data = list(plots)
        #(I could also add here an if statement to ID which column to take)
        for row in data[1:]:
            x.append(float(row[elev_col_num])) #sets elevations as x values
            y.append(float(row[dhdt_col_num])) #sets dh/dt med as y values
    plt.plot(x, y, label = glaciername)
    

#define settings for the plot
plt.xlabel('Elevation (m)')
plt.ylabel('dh/dt ')
plt.title('Glacier Height Change Across Elevation')
#plt.legend() 
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show() #reveals the plot
    
    

    