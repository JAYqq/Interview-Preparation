def main():
    n=int(input())
    nums=list(map(int,input().split(" ")))
    res=[]
    length=len(nums)
    for i in range(length):
        ans=1
        maxn=-1
        for j in range(i-1,-1,-1):
            if nums[j]>maxn:
                ans+=1
                maxn=nums[j]
        maxn=-1
        for j in range(i+1,length):
            if nums[j]>maxn:
                ans+=1
                maxn=nums[j]
        res.append(ans)
    for item in res:
        print(item,end=" ")
main()
