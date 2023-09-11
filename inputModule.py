# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:47:56 2023

@author: trent
"""
# checks if the input is a number for a loop with a boolan pass/fail
def passForNumber(numb):
    passing = 1
    try:
        numb = int(numb)
    except ValueError:
        try:
            numb = float(numb)            
        except:
            passing = 0
            print('please enter a number')
    return passing

def getInputNum():
    passing = 0
    while (passing == 0):
        numbOne = input('Enter number: ')
        passing = passForNumber(numbOne)
    return numbOne

def getInputNum():
    passing = 0
    while (passing == 0):
        numbOne = input('Enter Symbol: ')
        passing = passForNumber(numbOne)
    return numbOne

def getInputUnsafe():
    numbOne = input('Enter number: ')
    return numbOne