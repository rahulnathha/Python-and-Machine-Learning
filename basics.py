# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 05:05:14 2019

@author: rahul
"""
#%%
"""
Hello World
"""
msg="Hello World"
print(msg)

#%%
"""
User Input
"""

name = input("What's your name? ") 
print("Hello, " + name + "!")


#%%
"""
if elif else
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  

#%%
"""
while loop
"""

i = 1
while i < 6:
  print(i)
  i += 1
  
#%%
"""
for loop
"""

for x in "banana":
  print(x)
  

for x in range(2, 6):
  print(x)

#%%  
"""
Functions
"""

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India")
my_function()

#%%
"""
Classes
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 

#%%
"""
Exception handling
"""

try:
  print(q)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 
#%% 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  