dic={}
res={}
def main():
    # n,m=list(map(int,input().split(" ")))
    n=int(input())
    ans=0
    for i in range(n):
        p1,p2=input().split()
        if not dic.get(p1):
            dic[p1]=[p2]
        else:
            dic[p1].append(p2)
        res[p1]=False
    for key,val in res.items():
        if not val:
            res[key]=True
            for here in dic[key]:
                dfs(key,here)
                ans+=1
    print(ans)
def dfs(from_,to):
    if from_==to:
        return
    res[to]=True
    for item in dic[to]:
        dfs(from_,item)
main()