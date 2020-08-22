def main():
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[0 for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i]=arr[i]
    for i in range(1,len(arr)):
        dp[i]=max(dp[i],dp[i-1]+arr[i])
    maxn=-999999999
    for item in dp:
        maxn=max(maxn,item)
    print(maxn)
main()
