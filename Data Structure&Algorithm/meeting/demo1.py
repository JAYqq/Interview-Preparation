def main():
    fenzi=int(input())
    fenmu=int(input())
    dic={}
    ans=""
    target=""
    flag=False
    if fenzi>fenmu:
        temp=fenzi//fenmu
        ans+=str(temp)+'.'
        fenzi=fenzi%fenmu
    else:
        ans="0."
    while fenzi!=0:
        fenzi*=10
        if dic.get(fenzi):
            target=str(fenzi//fenmu)
            flag=True
            break
        dic[fenzi]=True
        temp=fenzi//fenmu
        fenzi=fenzi%fenmu
        ans+=str(temp)
    if flag:
        index=ans.index(target)
        ans=ans[0:index]+'('+ans[index::]+")"
    print(ans)

main()