def main():
    n,a,b=list(map(int,input().split()))
    arr=[]
    ans1,ans2=0,0
    for i in range(n):
        k1,k2=list(map(int,input().split()))
        arr.append((k1,k2))
    arr.sort(key=lambda x:x[0],reverse=True)
    for i in range(a):
        ans1+=arr[i][0]
    brr=arr[a:]
    brr.sort(key=lambda x:x[1],reverse=True)
    for i in range(b):
        ans1+=brr[i][1]
    #2
    arr.sort(key=lambda x:x[1],reverse=True)
    for i in range(b):
        ans2+=arr[i][0]
    brr=arr[a:]
    brr.sort(key=lambda x:x[0],reverse=True)
    for i in range(a):
        ans2+=brr[i][0]
    ans=max(ans1,ans2)
    print(ans)
main()



