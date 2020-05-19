#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:19:16 2020

@author: abhingude
"""

#Collecting data of a patient(General Data and Symptoms)
#Returns the Dictionary with keys as symptoms and its values
def patient_data():
    dl={}
    name=input("Please enter the patient's name : ")
    dl['Name']=name.upper()
    age=int(input("Enter the patient's age : "))
    dl['Age']=age
    b1=True
    temp=int(input("Temperature of the Patient in Fahrenheit : "))
    while b1:
        if(temp>82 and temp<110):
            dl['Temperature']=temp
            b1=False
        else:
            temp=int(input("Please enter temperature in Fahrenheit not Celsius : "))
    b1=True
    drycough=input("Is Patient having a dry cough (Yes/No) : ")
    while b1:
        drycough.lower()
        if(drycough=="yes" or drycough=="no"):
            dl['Dry Cough']=drycough
            b1=False
        else:
            drycough=input("Please enter only yes/no : ")
    b1=True
    print("Fatigue means tiredness,physically weak or lack of energy")
    fatigue=input("Is Patient feeling Fatigue (Yes/No) : ")
    while b1:
        fatigue.lower()
        if(fatigue=="yes" or fatigue=="no"):
            dl['Fatigue']=fatigue
            b1=False
        else:
            fatigue=input("Please enter only yes/no : ")
    b1=True
    print("Loss of appetite means you don't have the same desire to eat as you used to")
    loa=input("Is Patient feeling loss of appetite (Yes/No) : ")
    while b1:
        loa.lower()
        if(loa=="yes" or loa=="no"):
            dl['Loss Of Appetite']=loa
            b1=False
        else:
            loa=input("Please enter only yes/no : ")
    b1=True
    ba_values=["no","normal","high","extreme"]
    ba=input("Patients body aches range (no/normal/high/extreme) : ")
    while b1:
        ba.lower()
        if(ba in ba_values):
            dl['Body Aches']=ba
            b1=False
        else:
            ba=input("Please enter only no/normal/high/extreme : ")
    b1=True
    sob_values=["no","normal","high","extreme"]
    sob=input("Patients shortness of breath condition (no/normal/high/extreme) : ")
    while b1:
        sob.lower()
        if(sob in sob_values):
            dl['Shortness Of Breath']=sob
            b1=False
        else:
            sob=input("Please enter only no/normal/high/extreme : ")
    b1=True
    st=input("Is Patient having Sore Throat (Yes/No) : ")
    while b1:
        st.lower()
        if(st=="yes" or st=="no"):
            dl['Sore Throat']=st
            b1=False
        else:
            st=input("Please enter only yes/no : ")
    b1=True
    ha=input("Is Patient having headache (Yes/No) : ")
    while b1:
        ha.lower()
        if(ha=="yes" or ha=="no"):
            dl['Headache']=ha
            b1=False
        else:
            ha=input("Please enter only yes/no : ")
    b1=True
    lost=input("Does Patient experiencing loss of Smell/Taste (Yes/No) : ")
    while b1:
        lost.lower()
        if(lost=="yes" or lost=="no"):
            dl['Loss Of Smell/Taste']=lost
            b1=False
        else:
            lost=input("Please enter only yes/no : ")
    b1=True
    vom=input("Does Patient vomits (Yes/No) : ")
    while b1:
        vom.lower()
        if(vom=="yes" or vom=="no"):
            dl['Vomiting']=vom
            b1=False
        else:
            vom=input("Please enter only yes/no : ")
    return dl
    
    
            
    
    
            
            
        


k=patient_data()
print(k)
            
    
    
    
    
    