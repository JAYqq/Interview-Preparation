from typing import List
'''归并排序相比于快速排序的弱点在于temp数组，导致他不是一个原地排序算法，所以他需要O(n)的空间复杂度'''
def merge_sort(a:List[int]):
    merge_sort_between(a, 0, len(a) - 1)

def merge_sort_between(a:List[int],low:int,high:int):
    if low<high:
        mid=low+((high-low)>>1) #注意不能写成low+(high-low)>>2，因为python中的位运算符优先级比+低
        merge_sort_between(a,low,mid)
        merge_sort_between(a,mid+1,high)
        merge(a,low,mid,high)
def merge(a:List[int],low:int,mid:int,high:int):
    i,j=low,mid+1
    temp=[]
    while i<=mid and j<=high:
        if a[i]<=a[j]:
            temp.append(a[i])
            i+=1
        else:
            temp.append(a[j])
            j+=1
    start=i if i<=mid else j
    end=mid if i<=mid else high
    temp.extend(a[start:end+1])
    a[low:high+1]=temp
if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)