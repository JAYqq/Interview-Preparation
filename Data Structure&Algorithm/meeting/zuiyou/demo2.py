def main():
    n=int(input())
    dp=[0 for _ in range(16)]
    dp[0],dp[1],dp[2],dp[3]=1,1,2,5
    for i in range(4,16):
        temp=0
        for j in range(i):
            temp+=dp[j]*dp[i-j-1]
        dp[i]=temp
    if n==0:
        print(0)
    else:
        print(dp[n])
main()