# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 02:55:21 2019

@author: MA073146
"""

def main():
    print("The program starts")
 
    sum=0
    
    n=int(input("The number of inputs:  "))
    if n>0:
        for i in range(1,n+1):
            temp =i/(i+1)
            sum=sum+temp
    
    print("The desired output as per the sequence is:    "+str(sum))

        

            
main()