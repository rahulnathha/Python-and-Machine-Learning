# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:09:44 2019

@author: rahul
"""
#%%


'''Loading dataset'''
import numpy as np
import pandas as pd
dataset = pd.read_csv("cattdat.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
print(X)
#%%


'''Dealing with missing data'''
from sklearn.preprocessing import Imputer as imp
imputer = imp(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
#%%


'''Encoding Y'''
from sklearn.preprocessing import LabelEncoder as le
labelencoder_x = le()
X[:,3]=labelencoder_x.fit_transform(X[:,3])
#%%


'''Dummy variable'''
from sklearn.preprocessing import OneHotEncoder as hot
ohe = hot(categorical_features=[3])
X = ohe.fit_transform(X).toarray()

print(X)
#%%


'''Avoid dummy variable trap'''
X = X[:,1:]
#%%


'''Splitting the training and testing data'''
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)
#%%


'''Linear Regression'''
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, Y_train)
Y_predicted = regression.predict(X_test)

from sklearn.metrics import mean_absolute_error, explained_variance_score
print("Mean Absolute Error = "+str(mean_absolute_error(Y_test,Y_predicted)))
print(explained_variance_score(Y_test, Y_predicted))
'''See the Regression metrics section of the user guide for further details.

metrics.explained_variance_score(y_true, y_pred)	
metrics.max_error(y_true, y_pred)	
metrics.mean_absolute_error(y_true, y_pred)
metrics.mean_squared_error(y_true, y_pred[, …])
metrics.mean_squared_log_error(y_true, y_pred)
metrics.median_absolute_error(y_true, y_pred)
'''
#%%

'''Backward Elimination'''
import statsmodels.formula.api as model
X = np.append(arr = np.ones((300,1)).astype(int), values = X, axis = 1)
Optimus_X = X[:, 0:5]
regressor_ols = model.OLS(Y, Optimus_X).fit()
regressor_ols.summary()
Optimus_X = X[:, [0,1,3,4]]
regressor_ols = model.OLS(Y, Optimus_X).fit()
#print(p)
#%%
Optimus_X = X[:, [0,1,3,4]]
regressor_ols = model.OLS(Y, Optimus_X).fit()
regressor_ols.summary()
Optimus_X = X[:, [0,3,4,5]]
regressor_ols = model.OLS(Y, Optimus_X).fit()
regressor_ols.summary()
Optimus_X = X[:, [0,3,5]]
regressor_ols = model.OLS(Y, Optimus_X).fit()
p = regressor_ols.summary()
Optimus_X = X[:, [0,3]]
regressor_ols = model.OLS(Y, Optimus_X).fit()
p = regressor_ols.summary()