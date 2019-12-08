# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 02:01:04 2019
5,8
@author: MA073146
"""


def main():
    print("The program starts")
    input_list = []
    output_list= []
    
    
    n=int(input("The number of inputs:  "))
    
    for i in range(0,n):
        
        ele=input(("Input Value "+str(i+1)+":  "))
        try:
            int(ele)
            input_list.append(ele)
            output_list.append(ele)            
        except Exception:
            input_list.append(ele)
        
    print("Desired Output List:  ")
    print(output_list)
            
main()
            
            

            
            
            
    
