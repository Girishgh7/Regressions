import numpy as np 
import random as rd 
import matplotlib.pyplot as plt 
import pandas as pd

def loss_function(m,b,points):
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].time_study
        y=points.iloc[i].Marks
        total_error+=(y-(x*x+b))**2
    total_error/float(len(points))

def gradient_descent(m_now,b_now,points,l):
    m_gradient=0
    b_gradient=0
    n=len(points)
    for i in range(n):
        x=points.iloc[i].time_study
        y=points.iloc[i].Marks
        
        m_gradient+=-(2/n)*x*(y-(m_now*x + b_now))
        b_gradient+=-(2/n)*x*(y-(m_now*x + b_now))
    m=m_now-m_gradient*l
    b=b_now-b_gradient*l
    return m,b

data=pd.read_csv('Student_Marks.csv')


m=2
b=0
l=0.0002
epochs=1250
         
for i in range (epochs):
    if i%50==0:
        print(f"epochs:{i}")
    m,b=gradient_descent(m,b,data,l)  
print(m,b)
plt.scatter(data.time_study,data.Marks,color='red')
plt.plot(list(range(0,8)),[m*x+b for x in range(0,8)],color='black')
plt.show() 

