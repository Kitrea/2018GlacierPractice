#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:25:23 2018

@author: kitreatakataglushkoff

Need to make sure that if there are spread out points within ydata, they will 
still all be added.
"""
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#define variables
xdata = "# bin_center_elev_m"
ydata = " dhdt_bin_med_ma"

#define the path directory to pull files from
infile_path = r'/Users/kitreatakataglushkoff/Documents/All_Documents/SUMMER_2018/Glaciology/HiMAT/DEMs/mb_bins_sample_20180323'
region = str(15) #define the region of interest
region_files = glob.glob(infile_path+'/' + region + '*.csv')

#create a list of all glacier names in the region
all_names = []
for file in region_files: 
    #pull the name of the glacier from file title, store as a var
    path_list = file.split('/')
    file_name = path_list[-1]
    glaciername = str(file_name.split('_')[0]) #store each glacier RGI name into a var
    all_names.append(glaciername) #add each glacier name to a list of all names
print('Pandas will now create a dataframe containing values from the following glaciers: ', all_names)

#Create a dataframe that pulls in all necessary info
df = pd.DataFrame(np.zeros((882, (len(region_files)))), columns = all_names) #create an empty dataframe with 882 rows
df[df==0] = np.nan #change all zero values to NaN values
df.insert(loc=0, column='Elevation', value=range(5,8820,10)) #insert elevation column

#loop through each file of the desired region within the folder
for file in region_files:
    data = pd.read_csv(file) #use pandas to read the file
    first_elev_idx = int(((data[xdata][0])-5)/10) #define the index where the first elev bin
    print('Glacier ',glaciername, ': ', len(data[xdata]), 'data points, lowest elev bin height: ', data[xdata][0])
    #insert dh/dt values to df, starting at first corresponding elev bin index
    df.loc[first_elev_idx:first_elev_idx + len(data[xdata])-1, glaciername] = data[ydata].values 
print(df)
print('There are ', len(region_files), 'total measured glaciers in region', region)

plt.plot(x = 'Elevation', y = '15.10255', label = glaciername)