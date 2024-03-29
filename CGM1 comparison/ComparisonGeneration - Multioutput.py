# -*- coding: utf-8 -*-
"""
Created on Thu Aug 01 13:48:41 2019

@author: Samuel Liu - EUROP 2019

The aim of this document is to take in outputs of gait data and compare the two
visually in an automated fashion.

This file provides a general guideline on how to compare more than 2 outputs

"""

import pandas as pd
from FunctionsforComparisonMultiOutput import *


#Import file. 
#Instruction: please fill in the line below
file1 = pd.read_csv("HF059A08.csv",comment = '#')  
#file2 = pd.read_csv("namefile2.csv",comment = '#') if using multiple files

#Note: panda read csv is stupid and can't seem to work with comment lines 
#on a consistent basis. It worked perfectly fine on health child and patient 
#data but not healthy female despite the format being exactly the same. So if 
#it doesn't read Vicon Output file directly, then comment out the lines 
#indicating the various events by putting # in the first column

file1 = file1.fillna('0') #fill in the gaps within the data input file

objectname1 = "HF059"     #Instruction: Please put in the name of the subject
objectname2 = "cgm1.0"    #Instruction: Please ID the unique suffix
objectname3 = "cgm1.1"
#objectname4 - "cgm2.0" for more outputs from Vicon, provided that there is one
#file


#Data Extraction: 
#Step 1, find out the line in which the headings for all the bodypart's located
(m,n) = file1.shape
k = findline(m,n,file1)
 

#Step 2: divide the dataset into two parts. Note, some of the data involve sets
#of nine for defining coordinates.

method1,method2 = datasplit(k,n,file1,objectname1,objectname2)    
method3 = datapull1(k,n,file1,objectname3)
#method4 = datapull1(k,n,file1,objectname4)
#At this point, you should see method1 and method2 lists being created that 
#store lists of lists.
    
#Step 3: Find the angles that overlap and that we can compare
method1a,method2a = findsame(k,method1,method2)
method1a,method3a = findsame(k,method1,method3)
#could repeat for as many different cases as required

#At this point, you should see two variables named method1a and method2a
#with the same size and also the objects to be compared in the exact order

#Step 3.9: Converting all the strings into floating point values
method1a,method2a = floatconver(method1a,method2a,k,m)
method3a = floatconver3(method3a,k1,m1)
#repeat as needed

#Step 4: Compute the difference between the two in the comparable angles
#differencecalc is the series of functions that will be used 

#Step 5: Visualise the things you wanna visualise
#Step 5.1: Pelvis Angles: The pelvic angle comparisons require all three angle
#outputs.

#PelvisTilt(k,method1a,method2a)
#PelvisOb(k,method1a,method2a)
#PelvisRot(k,method1a,method2a)

#Step 5.2 Hip Angles
#HipFlex(k,method1a,method2a)
#Hipadduct(k,method1a,method2a)
#Hiprot(k,method1a,method2a)

#Step 5.3 Knee Angles
#kneeflex(k,method1a,method2a)
#kneevarus(k,method1a,method2a)
#kneerot(k,method1a,method2a)

#Step 5.4 Foot/Ankle Angles
#Ankleflex(k,method1a,method2a)
#AnkleAdd(k,method1a,method2a)
#FootProg(k,method1a,method2a)
