import numpy as np
import pandas as pd

df = pd.read_csv('C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv')

print(df[ (df['HRMONTH']==12) & (df['HRYEAR']==2019) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==1)  & (df['HRYEAR']==2019) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==1)  & (df['HRYEAR']==2020) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==2)  & (df['HRYEAR']==2020) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==3)  & (df['HRYEAR']==2020) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==4)  & (df['HRYEAR']==2020) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==5)  & (df['HRYEAR']==2020) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==6)  & (df['HRYEAR']==2020) ]['HRMONTH'].count())

print(df[ (df['HRMONTH']==12) & (df['HRYEAR']==2019)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==1)  & (df['HRYEAR']==2019)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==1)  & (df['HRYEAR']==2020)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==2)  & (df['HRYEAR']==2020)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==3)  & (df['HRYEAR']==2020)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==4)  & (df['HRYEAR']==2020)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==5)  & (df['HRYEAR']==2020)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==6)  & (df['HRYEAR']==2020)  &  ((df['WORKCODE']==6) ) ]['HRMONTH'].count())

print(df[ (df['HRMONTH']==1)  & (df['HRYEAR']==2019) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==12) & (df['HRYEAR']==2019) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==1)  & (df['HRYEAR']==2020) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==2)  & (df['HRYEAR']==2020) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==3)  & (df['HRYEAR']==2020) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==4)  & (df['HRYEAR']==2020) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==5)  & (df['HRYEAR']==2020) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==6)  & (df['HRYEAR']==2020) & ((df['WORKCODE']==7) ) ]['HRMONTH'].count())

'''
print(df[ (df['HRMONTH']==1)&((df['WORKCODE']==6) |(df['WORKCODE']==7)) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==2)&((df['WORKCODE']==6) |(df['WORKCODE']==7)) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==3)&((df['WORKCODE']==6) |(df['WORKCODE']==7)) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==4)&((df['WORKCODE']==6) |(df['WORKCODE']==7)) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==5)&((df['WORKCODE']==6) |(df['WORKCODE']==7)) ]['HRMONTH'].count())
print(df[ (df['HRMONTH']==6)&((df['WORKCODE']==6) |(df['WORKCODE']==7)) ]['HRMONTH'].count())
'''