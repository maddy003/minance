# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:37:18 2019

@author: MA073146
"""
import datetime
import calendar


def leap_year(year):
    
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else: return False

def extra_day(year):
    date='29 02 '+str(year)
    day= datetime.datetime.strptime(date, '%d %m %Y').weekday()
    print(year)
    print(calendar.day_name[day])
    
    
    
def main():
    print("The program starts")
    
    
    year= int(input('Enter the year:    '))
    year_up=year_down=year
    
    if(leap_year(year)): 
        extra_day(year)
    else:
        while True:
            year_up=year_up+1
            year_down=year_down-1
            if(leap_year(year_up)):
                extra_day(year_up)
                break
            if(leap_year(year_down)):
                extra_day(year_down)
                break
            


            
main()
      