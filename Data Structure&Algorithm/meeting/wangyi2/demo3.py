# sumn=0
# maxn=-1
# def main():
#     global sumn
#     arr=list(map(int,input().split()))
#     sumn=sum(arr)
#     if sumn%7==0:
#         print(sumn)
#     else:
#         arr.sort()
#         for i in range(1,len(arr)):
#             if helper(arr,i):
#                 break
#         print(maxn)
# def helper(arr,mark):
#     global maxn
#     for i in range(len(arr)-mark):
#         temp=sumn-sum(arr[i:i+mark])
#         if temp%7==0:
#             maxn=max(maxn,temp)
#             return True
#     return False
# main()
maxn=-1
def main():
    arr=list(map(int,input().split()))
    dfs(arr,0,0)
    print(maxn)
def dfs(arr,ans,index):
    global maxn
    if ans%7==0:
        maxn=max(maxn,ans)
        return
    for i in range(index,len(arr)):
        ans+=arr[i]
        dfs(arr,ans,i+1)
        ans-=arr[i]
main()