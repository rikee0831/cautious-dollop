# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:52:19 2020

@author: User
"""
A=float(input("input the coefficient of x**2"))
B=float(input("input the coefficient of x"))
C=float(input("input the coeffecient independant of x"))
def determinant():
    global A,B,C
    if (A**2)-(4*A*C)==0:
        oneroot()
    elif (B**2)-(4*A*C)>0:
        tworoot()
    else:
        imaginary()

def oneroot():
    x1=((-B)+(B**2-4*A*C))/2*A
    print(x1)
def tworoot(): 
      x1=((-B)+(B**2-4*A*C))/2*A
      x2=((-B)-(B**2-4*A*C))/2*A
      print(x1,x2)
def imaginary():  
     x1=((-B)+(B**2-4*A*C))/2*A
     x2=((-B)-(B**2-4*A*C))/2*A
     print(x1,x2)
determinant()     