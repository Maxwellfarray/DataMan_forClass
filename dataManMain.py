# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:25:14 2023

@author: tompkint0208
"""
import datamanMath as mMod
import inputModule as iMod
import dataManRecord as dMod
go = 1
control = ''
while go == 1:
    print("-------------")
    print("1 Use calculator.")
    print("2 Do math questions.")
    print("3 exit")
    print("-------------")
    control = input()
    match control:
        case "1":
            mMod.main()
            break;
        case '2':
            dMod.main()
            break;
        case '3':
            go = 0
            break;
        case _:
            print('please use only the given options')
