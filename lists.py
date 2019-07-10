# -*- coding: utf-8 -*-
"""
Introduction to Python 
"""
#%% 
"""
List comprehension
"""
x=[4,7,3,9]
squared=[num**2 for num in x] #[16, 49, 9, 81]
dec=[float(num) for num in x] #[4.0, 7.0, 3.0, 9.0]
print(squared) #[16, 49, 9, 81]

x.insert(2,10) #inserts value 10 at index 2
print(x) #[4, 7, 10, 3, 9]
#%%

"""
Array Slicing

"""
val=["Rahul","is","not","a","programmer"]
print(val[1:3]) #['is', 'not']
print(val[3]) #a
val.remove("not")
print(val) #['Rahul', 'is', 'a', 'programmer']
#%%
"""
String Slicing
"""     
name="python"     
print(name[4::]) #on
print(name[0::2]) #pto
print(name[::-1]) #nohtyp
print(name[:0:-2]) #nhy
#%%