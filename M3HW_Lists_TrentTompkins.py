# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:22:18 2023

@author: trent
"""
import ListMod as lMod
monthsTemp, monthList = lMod.monthTempGet()
maximum = monthsTemp.index(max(monthsTemp)) 
minimum = monthsTemp.index(min(monthsTemp))
average = sum(monthsTemp)/len(monthsTemp)
print()
print('Fayetteville , NC 2023 Temp')
print('--------------------------')
print('Month                 Temp')
print('--------------------------')
for i in range(len(monthList)):
    print("{:<20}".format(monthList[i]),monthsTemp[i])
print('Highest Tem: ' + str(monthsTemp[maximum]) + "(" + str(monthList[maximum]) + ")")
print('lowest Tem : ' + str(monthsTemp[minimum]) + "(" + str(monthList[minimum]) + ")")
print("Averege Tem: " + str(average))