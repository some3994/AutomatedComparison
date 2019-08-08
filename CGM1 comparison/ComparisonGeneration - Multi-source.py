# -*- coding: utf-8 -*-
"""
Created on Thu Aug 01 13:48:41 2019

@author: Samuel Liu - EUROP 2019

The aim of this document is to take in outputs of gait data and compare the two
visually in an automated fashion.

This file deals with comparison while sourcing results from two files. It can 
compare between two methods. The sample provided is by extracting the Vicon data
from Vicon output csv file and Output from Phil Dixon's code.

NOTE: Phil's code were edited to make the comparison easier:
the comment # are taken out from the output file
the names of the joints are altered to match that of Vicon Output


"""

import pandas as pd
from FunctionsforComparisonMulti import *


#Import file. 
#Instruction: please fill in the line below
file1 = pd.read_csv("HC154A10.csv") 
file2 = pd.read_csv('HC154_results.csv') 
#Note: panda read csv is stupid and can't seem to work with comment lines 
#on a consistent basis. It worked perfectly fine on health child and patient 
#data but not healthy female despite the format being exactly the same. So if 
#it doesn't read Vicon Output file directly, then comment out the lines 
#indicating the various events

file1 = file1.fillna('0') #fill in the gaps within the data input file
file2 = file2.fillna('0')

objectname1 = "HC154"     #Instruction: Please put in the name of the subject
objectname2 = "cgm1.0"    #Instruction: Please ID the unique suffix  and then 
#run the script.

#Temporary Data Storage initialization
method1 = []
Temp1 = []
method2 = []
Temp2 = []

#Data Extraction: 
#Step 1, find out the line in which the headings for all the bodypart's located
(m1,n1) = file1.shape
(m2,n2) = file2.shape

k1 = findline(m1,n1,file1)
k2 = findline(m2,n2,file2) 

#Step 2: divide the dataset into two parts. Note, some of the data involve sets
#of nine for defining coordinates.
method3 = datapull(k2,n2,file2)

method1,method2 = datasplit(k1,n1,file1,objectname1,objectname2)    
#At this point, you should see method1 and method2 lists being created that 
#store lists of lists.

    
#Step 3: Find the angles that overlap and that we can compare

method1,method3 = findsame2(k1,k2,method1,method3)
method1 = floatconver2(method1,k1,m1)
method3 = floatconver3(method3,k2,m2)

#At this point, you should see two variables named method1a and method2a
#with the same size and also the objects to be compared in the exact order

#Step 3.9: Converting all the strings into floating point values

#Step 4: Compute the difference between the two in the comparable angles
#differencecalc is the series of functions that will be used 

#Step 5: Visualise the things you wanna visualise
#Step 5.1: Pelvis Angles: The pelvic angle comparisons require all three angle
#outputs.

#PelvisTilt(k1,k2,method1,method3)
#PelvisOb(k1,k2,method1,method3)
#Note: Phil's code defines x as y and y as x


#PelvisRot(k1,k2,method1,method3)

#Step 5.2 Hip Angles
#HipFlex(k1,k2,method1,method3)
#Hipadduct(k1,k2,method1,method3)
#Hiprot(k1,k2,method1,method3)

#Step 5.3 Knee Angles
#kneeflex(k1,k2,method1,method3)
#kneevarus(k1,k2,method1,method3)
#kneerot(k1,k2,method1,method3)

#Step 5.4 Foot/Ankle Angles
Ankleflex(k1,k2,method1,method3)
AnkleAdd(k1,k2,method1,method3)
FootProg(k1,k2,method1,method3)
