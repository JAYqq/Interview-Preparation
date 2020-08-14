def main():
    word1=input()
    word2=input()
    dp=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        dp[i][0]=i
    for i in range(len(word2)+1):
        dp[0][i]=i
    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                add=dp[i-1][j]+1
                delete=dp[i][j-1]+1
                modi=dp[i-1][j-1]+1
                dp[i][j]=min(min(add,delete),modi)
    print(dp[len(word1)][len(word2)])
main()
