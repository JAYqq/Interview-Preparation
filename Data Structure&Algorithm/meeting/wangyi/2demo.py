def main():
    n=int(input())
    while n:
        m=int(input())
        arr=list(map(int,input().split(" ")))
        arr.sort(reverse=True)
        length=len(arr)
        res=99999999
        for i in range(length):
            base=arr[i]
            ans,goa=0,0
            for j in range(i+1,length):
                if ans+arr[j]<base:
                    ans+=arr[j]
                else:
                    base+=arr[j]
            if ans==base:
                res=min(res,goa)
        n-=1
        print(res)
main()
