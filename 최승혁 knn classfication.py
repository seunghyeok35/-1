# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6CDaX2L0i04oPVPpF_cPx8zY7_FRFAD
"""

import pandas as pd


targetUrl = "https://www.kaggle.com/datasets/alexandrepetit881234/fake-bills"

df2 = pd.read_csv(targetUrl, sep='\t')


import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(df2)
plt.show()

msno.bar(df2)
plt.show()

df2['<!DOCTYPE html>'].unique()

dummy = pd.get_dummies(df2)
dummy
dummy.info()

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)  


ohe.fit(df2[['<!DOCTYPE html>']])

AA = ohe.transform(df2[['<!DOCTYPE html>']])
AA=pd.DataFrame(AA)
AA.info()
AA[9].describe()
AA[9]==1
import numpy as np
AA.loc[AA[9]==1]=np.NaN
AA.info()
AA=AA.drop([9],axis=1)
AA.info()
##이 밑부분 부터는 오류가 나온 코드인데 잘 모르겠습니다.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df2) ##standardization 코드 연습한건데, data를 df2로 바꾼 것 뿐인데 왜 오류가 나는지 모르겠습니다..
print('결과1',scaler.mean_) 

print('결과2', scaler.transform(df2))

print('결과3',scaler.transform([[2, 2]]))
     


df_Customer2=df2.drop(['<!DOCTYPE html>'],axis=1)
df_Customer_cat = pd.concat([df_Customer2,AA], axis=1)
df_Customer_cat.head()
df_Customer_cat.columns = df_Customer_cat.columns.astype(str)
df_Customer3=df_Customer_cat.drop(['Gender'],axis=1) ## 이 부분 Gender를 뭐라고 써야 할 지 아무리 생각해도 모르겠습니다.


from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=3)

AAA=imputer.fit_transform(df_Customer2)  ##이 부분 왜 에러가 나는지 아무리 생각해도 모르겠습니다.

BBB=pd.DataFrame(AAA)

BBB.info()

