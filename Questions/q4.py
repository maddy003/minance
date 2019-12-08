# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 03:15:26 2019

@author: MA073146
"""

def main():
    print("The program starts")
    
     
    n=(input("String Input : "))
    output_list = []
    temp_list = []
    temp_list = n.split()
    size=len(temp_list)

    for i in range(0,size):
        ele=temp_list[i]
        
        try:
            int(ele)
            output_list.append(ele)       
        except Exception:
            continue
    print(output_list)

    

        

            
main()
 