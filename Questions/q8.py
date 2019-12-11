# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:02:59 2019

@author: MA073146

• Password has to be alpa numeric
• At least have 2 special symbols
• Max length of password is 16
• JSON Common set of Data's
"""
import q8list


def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True
    count = 0
    count_special = 0

    for i in q8list.nouns_list:
        if passwd == i:
            print("common noun")
            val = False
    for i in passwd:
        for j in SpecialSym:
            if i == j:
                count_special = count_special + 1

    if len(passwd) > 16:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if any(char.isupper() for char in passwd):
        count = count + 1

    if any(char.islower() for char in passwd):
        count = count + 1

    if count == 0:
        print("Should have a letter")
        val = False

    if count_special < 2:
        print("need 2 special char")
        val = False

    if val:
        return val

    # Main method


def main():
    passwd = input("Input Password")

    if password_check(passwd):
        print("Password is valid")
    else:
        print("Invalid Password !!")

    # Driver Code


if __name__ == '__main__':
    main()
