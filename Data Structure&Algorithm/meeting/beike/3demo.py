def main():
    n=int(input())
    arr=list(map(int,input().split(" ")))
    dp=[1 for _ in range(n+1)]
    long=[1 for _ in range(n+1)]
    dp[0]=arr[0]
    ans=-1
    res=9999999
    for i in range(1,n):
        if (arr[i]|dp[i-1])>arr[i]:
            dp[i]=(arr[i]|dp[i-1])
            long[i]=long[i-1]+1
        else:
            dp[i]=arr[i]
    for item in dp:
        ans=max(ans,item)
    for i in range(n):
        if dp[i]==ans:
            res=min(long[i],res)
    print(long)
    print(dp)
    print(res,ans)
main()