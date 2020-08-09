def main():
    m=int(input())
    while m:
        n,k=list(map(int,input().split(" ")))
        ans=0
        if k>n-k:
            ans=(n-k)
        else:
            temp=max(k-1,0)
            ans=min(n-k,temp)
        print(0,ans)
        m-=1
main()
