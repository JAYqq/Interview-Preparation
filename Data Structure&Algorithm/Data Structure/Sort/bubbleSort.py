#low to high
def bubbleSort1():
    arr=[1,5,6,4,8,7,2,1]
    leng=len(arr)
    flag=False
    for i in range(leng):
        flag=False
        for j in range(leng-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                flag=True
        if flag==False:
            break
    print(arr)

#high to low
def bubbleSort2():
    arr=[1,5,6,4,8,7,2,6]
    leng=len(arr)
    flag=False
    for i in range(leng):
        flag=False
        for j in range(leng-1,i,-1):
            if arr[j]>arr[j-1]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
                flag=True
        if flag==False:
            break
    print(arr)
if __name__ == "__main__":
    bubbleSort1()
    bubbleSort2()