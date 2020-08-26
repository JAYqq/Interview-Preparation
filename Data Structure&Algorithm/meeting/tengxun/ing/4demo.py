def main():
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[[0,0] for _ in range(n)]
    dp[0][0]=1
    dp[0][1]=arr[0]
    for i in range(1,n):
        dp[i][0]=dp[i-1][0]+1
        if arr[i]<=arr[i-1]:
            dp[i][1]=dp[i-1][1]
        else:
            dp[i][1]=dp[i-1][1]+(arr[i]-arr[i-1])
    print(min(dp[n-1][0],dp[n-1][1]))
main()
    
