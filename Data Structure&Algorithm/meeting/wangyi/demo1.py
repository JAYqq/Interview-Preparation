def main():
    arr=list(map(int,input().split(" ")))
    arr=sorted(arr,reverse=True)
    ans=0
    ans+=(arr[0]-arr[1])
    ans+=(arr[1]-arr[2])
    print(ans,end=" ") 
main()