# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 14:18:09 2019

@author: some3994
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
#Kinematic Differences
##############################################################################
def PelvisTilt(k,method1a,method2a):
    i = findbodypart('LPelvis',method2a,k)
    pelvis1,pelvis2 = datatake(method1a,method2a,k,i,0)
    #0 to extract data at normal index 1, 1 to extract data at normal index
    #2 and etc.. Don't @me lol @python
    #As the angles are defined as oppisites, use diffcalcadjustment1
    PelvTiltDif = differencecalc(pelvis1,pelvis2)
    Test_Dif = PelvTiltDif[k+10]
    
    if Test_Dif<1:                
        pass
    elif Test_Dif<90 and Test_Dif>1:
        PelvTiltDif = diffcalcadjustment1(pelvis1,pelvis2)
    elif Test_Dif>90 and Test_Dif<180:
        PelvTiltDif = diffcalcadjustment2(pelvis1,pelvis2,k)

    plotgraph(pelvis1,'Pelvic Tilt Angle 1',pelvis2,'Pelvic Tilt Angle 2',PelvTiltDif,'Pelvic Tilt Angle Dif','Frame','Degrees')        
        
def PelvisOb(k,method1a,method2a):
    i = findbodypart('LPelvis',method2a,k)
    pelvis1,pelvis2 = datatake(method1a,method2a,k,i,1)
    
    PelvObDif = differencecalc(pelvis1,pelvis2)
    Test_Dif = PelvObDif[k+10]
    
    if Test_Dif<1:                
        pass
    elif Test_Dif<90 and Test_Dif>1:
        PelvObDif = diffcalcadjustment1(pelvis1,pelvis2)
    elif Test_Dif>90 and Test_Dif<180:
        PelvObDif = diffcalcadjustment2(pelvis1,pelvis2,k)
        
    plt.figure()
    plotgraph(pelvis1,'Pelvic Obliquity Angle 1',pelvis2,'Pelvic Obliquity Angle 2',PelvObDif,'Pelvic Obliquity Angle Dif','Frame','Degrees')
    
def PelvisRot(k,method1a,method2a):
    i = findbodypart('LPelvis',method2a,k)
    pelvis1,pelvis2 = datatake(method1a,method2a,k,i,2)
    
    PelvRotDif = differencecalc(pelvis1,pelvis2)
    Test_Dif = PelvRotDif[k+10]
    
    if Test_Dif<1:                
        pass
    elif Test_Dif<90 and Test_Dif>1:
        PelvRotDif = diffcalcadjustment1(pelvis1,pelvis2)
    elif Test_Dif>90 and Test_Dif<180:
        PelvRotDif = diffcalcadjustment2(pelvis1,pelvis2,k)

    plt.figure()    
    plotgraph(pelvis1,'Pelvic Rotation Angle 1',pelvis2,'Pelvic Rotation Angle 2',PelvRotDif,'Pelvic Rotation Angle Dif','Frame','Degrees')
        
def HipFlex(k,method1a,method2a):
    i = findbodypart('LHipAngles',method2a,k)
    lhip1,lhip2 = datatake(method1a,method2a,k,i,0)
    lhipflexDif = differencecalc(lhip1,lhip2)
        
    plt.figure()
    plotgraph(lhip1,'Hip Flexion Angle 1',lhip2,'Hip Flexion Angle 2',lhipflexDif,'Left Hip Flexion Angle Dif','Frame','Degrees')
    
    i = findbodypart('RHipAngles',method2a,k)
    rhip1,rhip2 = datatake(method1a,method2a,k,i,0)
    rhipflexDif = differencecalc(rhip1,rhip2)
        
    plt.figure()
    plotgraph(rhip1,'Hip Flexion Angle 1',rhip2,'Hip Flexion Angle 2',rhipflexDif,'Right Hip Flexion Angle Dif','Frame','Degrees')
        
def Hipadduct(k,method1a,method2a):      
    i = findbodypart('LHipAngles',method2a,k)
    lhip1,lhip2 = datatake(method1a,method2a,k,i,1)
    lhipaddDif = differencecalc(lhip1,lhip2)
        
    plt.figure()
    plotgraph(lhip1,'Hip Adduction Angle 1',lhip2,'Hip Adduction Angle 2',lhipaddDif,'Left Hip Adduction Angle Dif','Frame','Degrees')
    
    i = findbodypart('RHipAngles',method2a,k)
    rhip1,rhip2 = datatake(method1a,method2a,k,i,1)
    rhipaddDif = differencecalc(rhip1,rhip2)
        
    plt.figure()
    plotgraph(rhip1,'Hip Adduction Angle 1',rhip2,'Hip Adductiton Angle 2',rhipaddDif,'Right Hip Adduction Angle Dif','Frame','Degrees')

def Hiprot(k,method1a,method2a):      
    i = findbodypart('LHipAngles',method2a,k)
    lhip1,lhip2 = datatake(method1a,method2a,k,i,2)
    lhiprotDif = differencecalc(lhip1,lhip2)
        
    plt.figure()
    plotgraph(lhip1,'Hip Rotation Angle 1',lhip2,'Hip Rotation Angle 2',lhiprotDif,'Left Hip Rotation Angle Dif','Frame','Degrees')
    
    i = findbodypart('RHipAngles',method2a,k)
    rhip1,rhip2 = datatake(method1a,method2a,k,i,2)
    rhiprotDif = differencecalc(rhip1,rhip2)
        
    plt.figure()
    plotgraph(rhip1,'Hip Rotation Angle 1',rhip2,'Hip Rotation Angle 2',rhiprotDif,'Right Hip Rotation Angle Dif','Frame','Degrees')

def kneeflex(k,method1a,method2a):
    i = findbodypart('LKneeAngles',method2a,k)
    lknee1,lknee2 = datatake(method1a,method2a,k,i,0)
    lkneeflexDif = differencecalc(lknee1,lknee2)
        
    plt.figure()
    plotgraph(lknee1,'Knee Flexion Angle 1',lknee2,'Knee Flexion Angle 2',lkneeflexDif,'Left Knee Flexion Angle Dif','Frame','Degrees')
    
    i = findbodypart('RKneeAngles',method2a,k)
    rknee1,rknee2 = datatake(method1a,method2a,k,i,0)
    rkneeflexDif = differencecalc(rknee1,rknee2)
        
    plt.figure()
    plotgraph(rknee1,'Knee Flexion Angle 1',rknee2,'Knee Flexion Angle 2',rkneeflexDif,'Right Knee Flexion Angle Dif','Frame','Degrees')

def kneevarus(k,method1a,method2a):
    i = findbodypart('LKneeAngles',method2a,k)
    lknee1,lknee2 = datatake(method1a,method2a,k,i,1)
    lkneevarDif = differencecalc(lknee1,lknee2)
        
    plt.figure()
    plotgraph(lknee1,'Knee Varus Angle 1',lknee2,'Knee Varus Angle 2',lkneevarDif,'Left Knee Varus Angle Dif','Frame','Degrees')
    
    i = findbodypart('RKneeAngles',method2a,k)
    rknee1,rknee2 = datatake(method1a,method2a,k,i,1)
    rkneevarDif = differencecalc(rknee1,rknee2)
        
    plt.figure()
    plotgraph(rknee1,'Knee Varus Angle 1',rknee2,'Knee Varus Angle 2',rkneevarDif,'Right Knee Varus Angle Dif','Frame','Degrees')

def kneerot(k,method1a,method2a):
    i = findbodypart('LKneeAngles',method2a,k)
    lknee1,lknee2 = datatake(method1a,method2a,k,i,2)
    lkneerotDif = differencecalc(lknee1,lknee2)
        
    plt.figure()
    plotgraph(lknee1,'Knee Rotation Angle 1',lknee2,'Knee Rotation Angle 2',lkneerotDif,'Left Knee Rotation Angle Dif','Frame','Degrees')
    
    i = findbodypart('RKneeAngles',method2a,k)
    rknee1,rknee2 = datatake(method1a,method2a,k,i,2)
    rkneerotDif = differencecalc(rknee1,rknee2)
        
    plt.figure()
    plotgraph(rknee1,'Knee Rotation Angle 1',rknee2,'Knee Rotation Angle 2',rkneerotDif,'Right Knee Rotation Angle Dif','Frame','Degrees')

def Ankleflex(k,method1a,method2a):
    i = findbodypart('LAnkleAngles',method2a,k)
    lank1,lank2 = datatake(method1a,method2a,k,i,0)
    lankdorsiflexDif = differencecalc(lank1,lank2)
        
    plt.figure()
    plotgraph(lank1,'Ankle Dorsiflexion Angle 1',lank2,'Ankle Dorsiflexion Angle 2',lankdorsiflexDif,'Left Ankle Dorsiflexion Angle Dif','Frame','Degrees')
    
    i = findbodypart('RAnkleAngles',method2a,k)
    rank1,rank2 = datatake(method1a,method2a,k,i,0)
    rankdorsiflexDif = differencecalc(rank1,rank2)
        
    plt.figure()
    plotgraph(rank1,'Ankle Dorsiflexion Angle 1',rank2,'Ankle Dorsiflexion Angle 2',rankdorsiflexDif,'Right Ankle Dorsiflexion Angle Dif','Frame','Degrees')

def AnkleAdd(k,method1a,method2a):
    i = findbodypart('LAnkleAngles',method2a,k)
    lank1,lank2 = datatake(method1a,method2a,k,i,2)
    lankaddDif = differencecalc(lank1,lank2)
        
    plt.figure()
    plotgraph(lank1,'Ankle Adduction Angle 1',lank2,'Ankle Adduction Angle 2',lankaddDif,'Left Ankle Adduction Angle Dif','Frame','Degrees')
    
    i = findbodypart('RAnkleAngles',method2a,k)
    rank1,rank2 = datatake(method1a,method2a,k,i,2)
    rankaddDif = differencecalc(rank1,rank2)
        
    plt.figure()
    plotgraph(rank1,'Ankle Adduction Angle 1',rank2,'Ankle Adduction Angle 2',rankaddDif,'Right Ankle Adduuction Angle Dif','Frame','Degrees')

def FootProg(k,method1a,method2a):
    i = findbodypart('LFootProgress',method2a,k)
    lfoot1,lfoot2 = datatake(method1a,method2a,k,i,2)
    lfootprogDif = diffcalcadjustment3(lfoot2,lfoot1,k)
        
    plt.figure()
    plotgraph(lfoot1,'Foot Progression Angle 1',lfoot2,'Foot Progression Angle 2',lfootprogDif,'Left Foot Progression Angle Dif','Frame','Degrees')
    #Note: Always something strange happening with the last 16 data points
    
    i = findbodypart('RFootProgress',method2a,k)
    rfoot1,rfoot2 = datatake(method1a,method2a,k,i,2)
    rfootprogDif = diffcalcadjustment1(rfoot1,rfoot2)
        
    plt.figure()
    plotgraph(rfoot1,'Foot Progression Angle 1',rfoot2,'Foot Progression Angle 2',rfootprogDif,'Right Foot Progression Angle Dif','Frame','Degrees')

##############################################################################
def findline(m,n,file1):
    for i in range(m):
        if 'Frame' in file1.iloc[i,0]:
            break
        else:
            continue
    
    return i-1
    
def datasplit(k,n,file1,objectname1,objectname2):
    method1 = []
    Temp1 = []
    method2 = []
    Temp2 = []
    
    for i in range(n-3):
        if objectname2 in file1.iloc[k,i]: 
            #if the special suffix is found, data extracted
            Temp2.append(file1.iloc[k::,i])   #the columns are taken and stored
            Temp2.append(file1.iloc[k::,i+1])
            Temp2.append(file1.iloc[k::,i+2])
            if file1.iloc[k,i+3] == '0':
                Temp2.append(file1.iloc[k::,i+3])
                Temp2.append(file1.iloc[k::,i+4])
                Temp2.append(file1.iloc[k::,i+5])
                Temp2.append(file1.iloc[k::,i+6])
                Temp2.append(file1.iloc[k::,i+7])
                Temp2.append(file1.iloc[k::,i+8])
        
            method2.append(Temp2)
            Temp2 = [] 
            continue

        elif objectname2 not in file1.iloc[k,i] and objectname1 in file1.iloc[k,i]:
            Temp1.append(file1.iloc[k::,i])   
            Temp1.append(file1.iloc[k::,i+1])
            Temp1.append(file1.iloc[k::,i+2])
            #the XYZ columns are taken and stored in method1
            if file1.iloc[k,i+3] == '0':
                Temp1.append(file1.iloc[k::,i+3])
                Temp1.append(file1.iloc[k::,i+4])
                Temp1.append(file1.iloc[k::,i+5])
                Temp1.append(file1.iloc[k::,i+6])
                Temp1.append(file1.iloc[k::,i+7])
                Temp1.append(file1.iloc[k::,i+8])
                #Some of the outputs involve coordinates of 3 different points
                   
            method1.append(Temp1)
            #print('h')  
            Temp1 = []
            continue

    return method1,method2
        
    #an Index out of bounds error showed despite all the useful data being 
    #collected, hence error handling used to ignore the erroor and the last 
    #three columns are added on at the end.
        
def datapull(k,n2,file2):
    method3 = []
    Temp3 = []
    
    for i in range((n2-1)/3):
        Temp3.append(file2.iloc[k::,3*i+1])   #the columns are taken and stored
        Temp3.append(file2.iloc[k::,3*i+2])
        Temp3.append(file2.iloc[k::,3*i+3])
        
        method3.append(Temp3)
        Temp3 = [] 
    
    return method3

def findsame(k,method1,method2):
    method1a = []   #A new list to store the objects we can compare
    method2a = []
    
    for i in range(len(method1)):
        for j in range(len(method2)):
            if method1[i][0][k] in method2[j][0][k]:
                method1a.append(method1[i])
                method2a.append(method2[j])
                continue
            else:
                continue
    return method1a,method2a

def findsame2(k1,k2,method1,method3):
    method1a = []   #A new list to store the objects we can compare
    method3a = []
    
    for i in range(len(method1)):
        for j in range(len(method3)):
            if method3[j][0][k2] in method1[i][0][k1]:
                method1a.append(method1[i])
                method3a.append(method3[j])
                continue
            else:
                continue
    return method1a,method3a

def floatconver(method1a,method2a,k,m):    
    for i in range(len(method1a)):
        for j in range(k+3,m):        
            method1a[i][0][j] = float(method1a[i][0][j])
            method1a[i][1][j] = float(method1a[i][1][j])
            method1a[i][2][j] = float(method1a[i][2][j])
            method2a[i][0][j] = float(method2a[i][0][j])
            method2a[i][1][j] = float(method2a[i][1][j])
            method2a[i][2][j] = float(method2a[i][2][j])
    return method1a,method2a            

def floatconver2(method1a,k1,m1):    
    for i in range(len(method1a)):
        for j in range(k1+3,m1):        
            method1a[i][0][j] = float(method1a[i][0][j])
            method1a[i][1][j] = float(method1a[i][1][j])
            method1a[i][2][j] = float(method1a[i][2][j])
        
    return method1a

##############################################################################
#Difference Calculation functions: When the angles are defined differently in
#pelvis and foot progression angles, you can change the processing of the actual
#angle difference here by using one of the three functions here. Maybe it could
#have been detected automatically but really it ain't much effort to change
##############################################################################        

def differencecalc(array1,array2):
    difference = np.subtract(array1,array2)
    return difference
           
def diffcalcadjustment1(array1,array2):
    difference = np.add(array1,array2)
    return difference

def diffcalcadjustment2(array1,array2,k):
    for i in range(k+3,len(array1)+k+3):
        array2[i] = array2[i] - 180
    
    difference = np.subtract(array1,array2)
    return difference

def diffcalcadjustment3(array1,array2,k):
    for i in range(k+3,len(array1)+k+3):
        array2[i] = -1*array2[i] - 180
    
    difference = np.subtract(array1,array2)
    return difference

def diffcalcadjustment4(array1,array2,k):
    for i in range(k+3,len(array1)+k+3):
        array1[i] = array1[i] - 360
    
    difference = np.subtract(array1,array2)
    return difference
##############################################################################
#Bodypart finding functions
##############################################################################    
def findbodypart(stringbody,method2a,k):
    for i in range(len(method2a)):
        if stringbody in method2a[i][0][k]:
            break
    return i

##############################################################################
#Data taking functions
##############################################################################

def datatake(method1a,method2a,k,i,xyz):
    data1 = method1a[i][xyz][3::]
    data2 = method2a[i][xyz][3::]
    return data1,data2

##############################################################################
#Plots
##############################################################################
    
def plotgraph(list1,label1,list2,label2,difference,label3,whatx,whaty):
    plt.subplot(211)
    plt.plot(list1,'b',label = label1)
    plt.plot(list2,'r',label = label2)
    #plt.xlabel(whatx)
    plt.ylabel(whaty)
    plt.legend
    plt.title(label1 + ' and ' + label2 + ' Comparison Graph')
    
    plt.subplot(212)    
    plt.plot(difference,label = label3)
    plt.xlabel(whatx)
    plt.ylabel(whaty)
    plt.legend
    plt.title(label3 + ' between Two Methods')
    
