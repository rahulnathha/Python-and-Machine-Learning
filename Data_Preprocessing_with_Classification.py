# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:48:11 2019

@author: rahul
"""
#%%
import warnings
warnings.filterwarnings("ignore")


#%%
import pandas as pd
'''Loading dataset'''
dataset = pd.read_csv("Preprodata.csv")                                                    


#%%
'''Dealing with missing data'''
#dataset.dropna(how = 'any', inplace = True)   
#dataset.fillna(dataset.mean() ,inplace=True)
#dataset.fillna(dataset.mode() ,inplace=True)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
print(X)
print(Y)
print()
print()
from sklearn.preprocessing import Imputer
imputer_object = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
X[:,[1,4]] = imputer_object.fit_transform(X[:,[1,4]])
imputer_object = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 0)
X[:,[2,3,5]] = imputer_object.fit_transform(X[:,[2,3,5]])
print(X)


#%%
'''Encoding X'''
from sklearn.preprocessing import LabelEncoder
labelencoder_for_x = LabelEncoder()
X[:,0]=labelencoder_for_x.fit_transform(X[:,0])
print(X)


#%%
'''Dummy Variables'''
from sklearn.preprocessing import OneHotEncoder
one_hot_encoder_for_X = OneHotEncoder(categorical_features = [0])
X = one_hot_encoder_for_X.fit_transform(X).toarray()


#%%
'''Encoding Y'''
labelencoder_for_y = LabelEncoder()
Y=labelencoder_for_y.fit_transform(Y)


#%%
'''Splitting the training and testing data'''
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)
print(X)
print(Y)


#%%
'''Scaling X Values'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#%%
'''Classifiers'''
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,Y_train)
Y_predicted = knn.predict(X_test)
print(Y_predicted)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_predicted))