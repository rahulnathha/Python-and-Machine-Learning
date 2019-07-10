# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 05:57:47 2019

@author: rahul
"""
import pandas as pd
from sklearn.cross_validation import train_test_split

'''Loading dataset'''
dataset = pd.read_csv("_LinearRegdata.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

'''Train and Test Split'''
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.33, random_state = 0)
print(X)
print(Y)
#print("success")


#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_predicted = regressor.predict(X_test)
print(Y_predicted)

#Visualising
import matplotlib.pyplot as plt
plt.figure(figsize = (10,10))

plt.scatter(Y_test, Y_predicted, color = ["red", "black"])
plt.show()
plt.figure(figsize = (10,10))
plt.scatter(X_train, Y_train, c ="red")
plt.plot(X_train, regressor.predict(X_train), label = "regressorplot")
plt.legend(loc = "lower right") # ---> the line constructed!!!
plt.title("Trainging values vs Predicted Values of Training data")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()