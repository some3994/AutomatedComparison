# -*- coding: utf-8 -*-
"""
Created on Thu Aug 01 13:48:41 2019

@author: Samuel Liu - EUROP 2019

The aim of this document is to take in outputs of gait data and compare the two
visually in an automated fashion.

This file deals with comparison using Vicon outputs for CGM1. It can compare 
between two methods

"""

import pandas as pd
from FunctionsforComparison import *


#Import file. 
#Instruction: please fill in the line below
file1 = pd.read_csv("HF059A08.csv",comment = '#')  
#Note: panda read csv is #### and can't seem to work with comment lines 
#on a consistent basis. It worked perfectly fine on health child and patient 
#data but not healthy female despite the format being exactly the same. So if 
#it doesn't read Vicon Output file directly, then comment out the lines 
#indicating the various events at the start of the document

file1 = file1.fillna('0') #fill in the gaps within the data input file

objectname1 = "HF059"     #Instruction: Please put in the name of the subject
objectname2 = "cgm1.0"    #Instruction: Please ID the unique suffix  and then 
#run the script.

#Temporary Data Storage initialization
method1 = []
Temp1 = []
method2 = []
Temp2 = []

#Data Extraction: 
#Step 1, find out the line in which the headings for all the bodypart's located
(m,n) = file1.shape
k = findline(m,n,file1)
 

#Step 2: divide the dataset into two parts. Note, some of the data involve sets
#of nine for defining coordinates.

method1,method2 = datasplit(k,n,file1,objectname1,objectname2)    
#At this point, you should see method1 and method2 lists being created that 
#store lists of lists.
    
#Step 3: Find the angles that overlap and that we can compare
method1a,method2a = findsame(k,method1,method2)

#At this point, you should see two variables named method1a and method2a
#with the same size and also the objects to be compared in the exact order

#Step 3.9: Converting all the strings into floating point values
method1a,method2a = floatconver(method1a,method2a,k,m)

#Step 4: Compute the difference between the two in the comparable angles
#differencecalc is the series of functions that will be used 

#Step 5: Visualise the things you wanna visualise
#Step 5.1: Pelvis Angles: The pelvic angle comparisons require all three angle
#outputs.

PelvisTilt(k,method1a,method2a)
PelvisOb(k,method1a,method2a)
PelvisRot(k,method1a,method2a)

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
