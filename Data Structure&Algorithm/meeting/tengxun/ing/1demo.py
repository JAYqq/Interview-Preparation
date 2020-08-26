def main():
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        if i==k-1:
            continue
        if i==len(arr)-1:
            print(arr[i])
        else:
            print(arr[i],end=" ")

main()