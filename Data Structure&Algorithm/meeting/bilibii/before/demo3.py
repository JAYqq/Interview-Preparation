def main():
    n=int(input())
    m=int(input())
    w=list(map(int,input().split(" ")))
    v=list(map(int,input().split(" ")))
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if j>=w[i-1]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[n][m])
main()