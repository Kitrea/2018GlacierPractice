#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:39:39 2018

@author: kitreatakataglushkoff


This program will take an input csv file, and return the mb in w.e. per year, 
over the entire glacier
"""

import csv

area_col_num = 2 #user inputs the column number corresponding to bin valid areas
mbal_col_num = 11 #user inputs the col number corresponding to bin mb medians

def get_mbal():
    #open input csv file to read
    with open('Sampleglacier1_mb_bins.csv', 'r') as csv_input:
        #reads the file into 'data'
        data = csv.reader(csv_input, delimiter = ',')
        #turns the file into a list of rows
        data_list = list(data) 
        #define local variables
        total_area = 0.0
        total_mbal_area = 0.0
        overall_mbal = 0.0
        #loop through each rows(corresponding to each elevation bin), 
            #excluding the first title row
        for row in data_list[1:]:
            z1area = float(row[area_col_num]) #store the z1 valid area to var
            mbal = float(row[mbal_col_num]) #store the mbal med to var
            mbal_area = (z1area)*(mbal) #multiply the bin's mbal*area
            total_area += float(z1area) #keep track of total glacier area
            total_mbal_area += mbal_area #aggregate the (mbal*area) values
            
        print('Total Area = ', total_area) 
        print('Total Mass Balance Weighted Over Bin Areas = ',total_mbal_area)
        overall_mbal = total_mbal_area/total_area
    return overall_mbal #output: glacier's overall mass balance
    #for this file, the overall_mb should be 0.38

glacier_mbal = get_mbal() #store overall mass balance to a var