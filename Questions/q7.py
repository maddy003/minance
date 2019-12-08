# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:37:44 2019

@author: MA073146
"""

def main():
    print("The program starts")
    input_list = []
    output_list= []
    
    
    input_string=input("Enter a list numbers or elements separated by space: ")
    temp_list = input_string.split() 
    input_list = list(map(int, temp_list))    
    print(input_list)

    output_list=[i for i in input_list if i%2 !=0]


       
    print("Desired Output List:  ")
    print(output_list)
            
main()