ans=set()
res=[]
k=0
def main():
    global k,ans,res
    s=input()
    k=int(input())
    temp_arr=[]
    for i in range(len(s)):
        temp_arr.append((i,s[i]))
    temp_arr.sort(key=lambda x:x[1])
    for item in temp_arr:
        dfs(item[0],s)
    ans=list(ans)
    ans.sort()
    print(ans[k-1])
def dfs(i,s):
    for j in range(i+1,len(s)):
        if len(ans)<=k:
            ans.add(s[i:j])
main()