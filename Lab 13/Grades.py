#Nathan Gregorian Bailey
#Section 0003
#Program 13
#Created on December 4th 2021 
#Due December 10th 2021
import math

def total(values):
    total_values = float(0)
    for i in values:
        total_values += i
    return total_values

def average(values):
    if len(values) == 0:
        return math.nan
    average_values = float(0)
    count = len(values)
    for i in values:
        average_values += i
    return average_values/count

def median(values):
    if len(values) == 0:
        raise ValueError
    slist = sorted(values)
    if len(slist)%2 == 1:
        return slist[len(slist)//2]
    if len(slist)%2 == 0 and len(slist)!= 0:
        return (slist[int((len(slist)/2)-1)] + slist[int(len(slist)/2)])/2