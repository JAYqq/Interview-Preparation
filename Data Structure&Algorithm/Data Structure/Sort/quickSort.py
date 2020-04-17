#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: willard
'''

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort1(array,low,high):
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort1(array,low,key_index)
        quick_sort1(array,key_index+1,high)

if __name__ == '__main__':
    array1 = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
    # # array1 = [5,4,3,2,1]
    #            1 4 3 2 4
    #            1 4 3 2 3
    #            1 4 3 2 2
    print (array1)
    quick_sort1(array1,0,len(array1)-1)
    print (array1)