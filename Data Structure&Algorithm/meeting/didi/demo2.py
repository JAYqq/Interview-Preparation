# def main():
#     n,m=list(map(int,input().split()))
#     table=list(map(int,input().split()))
#     custmer=[]
#     s=sum(table)
#     for _ in range(m):
#         temp=list(map(int,input().split()))
#         custmer.append(temp)
#     dp=[[0 for _ in range(s+1)] for _ in range(m+1)]
#     # for i in range()
#     for i in range(1,m):
#         for j in range(s+1):
#             if j>=custmer[i][0]:
#                 dp[i][j]=max(dp[i-1][j-custmer[i][0]]+custmer[i][1],dp[i-1][j])
#             else:
#                 dp[i][j]=dp[i-1][j]
#     print(dp[m-1][s])
# main()
'''
3 5 
2 4 2 
1 3 
3 5 
3 7 
5 9 
1 10
'''
def main():
    n,m=list(map(int,input().split()))
    table=list(map(int,input().split()))
    table.sort()
    res={}
    custmer=[]
    for _ in range(m):
        temp=list(map(int,input().split()))
        custmer.append(temp)
    custmer.sort(key=lambda x:x[0],reverse=True)
    for cus in custmer:
        



