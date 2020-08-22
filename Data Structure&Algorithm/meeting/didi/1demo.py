ans=[]
def main():
    n=int(input())
    dic,res={},[]
    dfs(n,dic,res)
    print(len(ans))
    for item in ans:
        print(item[0],item[1])
def dfs(n,dic,res):
    if len(res)==3 and res[0]!='0':
        if judge(res,n):
            temp=[int(res[0]+res[1]+res[2]),int(res[0]+res[2]+res[2])]
            ans.append(temp)
        return
    if len(res)==3 and res[0]=='0':
        return
    if res and res[0]=='0':
        return
    for i in range(10):
        if dic.get(i):
            continue
        dic[i]=1
        res.append(str(i))
        dfs(n,dic,res)
        dic[i]=0
        res.remove(str(i))

def judge(res,n):
    if int(res[0]+res[1]+res[2])+int(res[0]+res[2]+res[2])==n:
        return True
    else:
        return False

main()