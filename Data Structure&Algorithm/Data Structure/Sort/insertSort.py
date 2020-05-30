#low to high
def insertSort1():
    arr=[6,5,6,4,8,7,2,6]
    leng=len(arr)
    for i in range(1,leng):
        value=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>value:
                arr[j+1]=arr[j]
            else:
                break
        arr[j]=value
    print(arr)

#high to low
def insertSort2():
    arr=[1,5,6,4,8,7,2,6]
    leng=len(arr)
    for i in range(1,leng):
        value=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]<value:
                arr[j+1]=arr[j]
            else:
                break
        arr[j]=value #because the function of range won't decreace once again in last cycle,
                    #the value of arr[j] equal with arr[j+1],so we need to assign value to arr[j]
    print(arr)
if __name__ == "__main__":
    insertSort1()
    insertSort2()