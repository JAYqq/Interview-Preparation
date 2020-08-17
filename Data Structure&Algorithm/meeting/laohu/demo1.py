import sys
def main():
    res=set()
    line = sys.stdin.readline().strip()
    n,k=list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    arr=list(map(int, line.split()))
    left,right=0,n-1
    while left<right:
        if arr[left]+arr[right]==k:
            res.add((arr[left],arr[right]))
            left+=1
            right-=1
        if arr[left]+arr[right]<k:
            left+=1
        if arr[left]+arr[right]>k:
            right-=1
    # print(res)
    res=list(res)
    res.sort()
    for item in res:
        print(item[0],item[1])
main()