def main():
    num=int(input())
    for i in range(1,num):
        dfs(num,0,i)
ans=0
def dfs(num,res,k):
    global ans
    if res==num:
        ans+=1
        return
    if res>num:
        return
    dfs(num,res+k,k+1)
main()
print(ans+1)
