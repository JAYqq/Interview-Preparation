def main():
    t=int(input())
    while t:
        n=int(input())
        print(handle(n))
        t-=1
def count(n):
    a=n
    cn_ll=0
    while a:
        cn_ll+=1
        a>>=1
    return cn_ll
def count_cn1(n):
    a=n
    cn1=0
    while a:
        if a&1==1:
            cn1+=1
        a>>=1
    return cn1
def handle(n):
    ans,res=0,-1
    cn_all=count(n)
    print(cn_all)
    base=2**(cn_all-1)
    for i in range(base,n):
        if count(i)==cn_all:
            temp=count_cn1(i)
            if ans<temp:
                ans=temp
                res=i
    return res
main()