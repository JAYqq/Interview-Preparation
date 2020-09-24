def main():
    n,p=list(map(int,input().split()))
    inp=[]
    for i in range(n):
        a,b,c=list(map(int,input().split()))
        temp=[a,b,c,c/b]
        inp.append(temp)
    inp.sort(key=lambda x: x[3],reverse=True)
    ans=0
    for item in inp:
        num=p//item[1]
        if num<=item[0]:
            ans+=num*item[2]
            p-=num*item[1]
        else:
            ans+=item[0]*item[2]
            p-=item[0]*item[1]
    print(ans)
main()