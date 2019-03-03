# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:11:55 2019

@author: admin
"""

#from <package> import <module> as <nickname>
import pandas as pd
from  matplotlib import pyplot as plt
x=[1,2,3]
y=[4,5,6]
z=[10,11,12]
plt.plot(x,y)
plt.plot(x,z)
plt.title("TEST")
#plt.xlabel("X")
#plt.ylabel("Y and Z")
plt.legend(["this is x", "This is y"])
plt.show()

#plt.show is used to end the plot for a particular data

sampledata = pd.read_csv("sample_data.csv")
#print((sampledata))

#for accessing single column, use dot operator
#print(sampledata.column_c)

#for accessing single element, use iloc
print(sampledata.column_c.iloc[1])
plt.plot(sampledata.column_a,sampledata.column_b, 'o')
plt.plot(sampledata.column_a,sampledata.column_c, 'o')
plt.legend(["this is x", "This is y", "that one is sexy"])
plt.show()


realsam = pd.read_csv("countries.csv")
print(realsam)
#accessing particular rows, just give a true false statement
In=realsam[realsam.country == 'India']
ini=In.population.iloc[0]
Us=realsam[realsam.country == 'United States']
uni=Us.population.iloc[0]
plt.plot(In.year,In.population/ini-1)
plt.plot(Us.year,Us.population/uni-1)
plt.legend(["INDIA","USA"])
#plt.xlabel('Year')
#plt.ylabel('Population in millions')
plt.show()
