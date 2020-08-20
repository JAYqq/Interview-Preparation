# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# '''
# @author: willard
# '''
import random
# def sub_sort(array,low,high):
#     key = array[low]
#     while low < high:
#         while low < high and array[high] <= key:
#             high -= 1
#         while low < high and array[high] > key:
#             array[low] = array[high]
#             low += 1
#             array[high] = array[low]
#     array[low] = key
#     return low


# def quick_sort1(array,low,high):
#     if low <high:
#         cu=random.randint(low,high)
#         array[low],array[cu]=array[cu],array[low]
#         key_index = sub_sort(array,low,high)
#         quick_sort1(array,low,key_index)
#         quick_sort1(array,key_index+1,high)

# if __name__ == '__main__':
#     array1 = [3,2,1,5,6,4,4,4]
#     #array1 = [5,4,3,2,1]
#     #            1 4 3 2 4
#     #            1 4 3 2 3
#     #            1 4 3 2 2
#     print (array1)
#     quick_sort1(array1,0,len(array1)-1)
#     print (array1)

def sub_sort(arr,low,high):
    temp=arr[low]
    while low<high:
        while low<high and arr[high]>=temp:
            high-=1
        while low<high and arr[high]<temp:
            arr[low]=arr[high]
            low+=1
            arr[high]=arr[low]
    arr[low]=temp
    return low
def quick_sort(arr,low,high):
    if low<high:
        cur=random.randint(low,high)
        arr[low],arr[cur]=arr[cur],arr[low]
        index = sub_sort(arr,low,high)
        quick_sort(arr,low,index)
        quick_sort(arr,index+1,high)

if __name__ == '__main__':
    array1 = [3,2,1,5,6,4,4,4]
    #array1 = [5,4,3,2,1]
    #            1 4 3 2 4
    #            1 4 3 2 3
    #            1 4 3 2 2
    print (array1)
    quick_sort(array1,0,len(array1)-1)
    print (array1)



