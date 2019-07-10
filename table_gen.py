# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:48:53 2019

@author: rahul
"""
import random as r

#%%
'''Classification Data'''
arr = ["India","Chinese", "Japanese"]
marr = ["yes","no"]
files= open("_Preprodata.csv","w")
files.write("Citizenship, Salary, Age, Houses Owned, Bank Balance, Cars Owned, Married \n")
for i in range(300):
    string = arr[r.randint(0,2)]+","+str(r.randint(50000, 500000))+","+ \
    str(r.randint(20,60))+","+str(r.randint(0,3))+","+str(r.randint(500000,50000000))+ \
    ","+str(r.randint(0,2))+","+marr[r.randint(0,1)]+"\n"
    files.write(string)
files.close()
#%%
'''Simple Linear Regression Data'''
files= open("_LinearRegdata.csv","w")
files.write("Kilometers, Life \n")
for i in range(200):
    kms = r.randint(2000,20000)
    life = (abs(kms-r.uniform(7000.0,11000.0)))/18000.0 + r.uniform(1.5,2.0)
    string = str(kms) + "," + str(life) + "\n"
    print(string)
    files.write(string)
files.close()
#%%
import random as r
'''Multiple Linear Regression'''
arrind = ["Uttar Pradesh","Rajasthan", "Kerala"]
diction = {"Uttar Pradesh":1.5,"Rajasthan":1.4,"Kerala":1}
f = [1,-1]
files= open("_cattledata.csv","w")
files.write("Amount of Feed, Amount of Water, Man Power Input, State, Sales Value \n")
for i in range(300):
    
    feed = r.uniform(30000,100000)
    water = r.uniform(50000,150000) 
    man_power_expense = r.uniform(50000,150000) 
    state = arrind[r.randint(0,2)]
    sales_value = (feed/1000 + (0.8*water/1000) + \
    (0.2*f[r.randint(0,1)]*water/1000) + \
    r.uniform(0.5,0.8)*man_power_expense)*\
    diction[state] + r.uniform(0,1000)
    sales_value = round(sales_value,1)
    string2 = str(feed) + "," + \
    str(water) + "," + \
    str(man_power_expense) + "," + \
    state + "," + \
    str(sales_value) + "," + "\n"
    
    files.write(string2)
files.close()