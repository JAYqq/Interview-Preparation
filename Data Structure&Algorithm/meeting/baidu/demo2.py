import random
random.randint
mmp=[]
def find(arr,target):
    # global mmp
    left,right=0,len(arr)-1
    ans=float("INF")
    while left<right:
        mid=left+(right-left)//2
        if arr[mid]<target:
            left=mid+1
        else:
            if not mmp[mid]:
                left=mid+1
                continue
            else:
                ans=min(mid,ans)
                right=mid
    if arr[left]>=target:
        ans=min(left,ans)
    if ans==float("INF"):
        return False
    else:
        return ans
def main():
    global mmp
    t=int(input())
    while t:
        n,m=list(map(int,input().split()))
        guys=list(map(int,input().split()))
        res=[]
        mmp=[True for _ in range(m)]
        orders=list(map(int,input().split()))
        orders.sort()
        for item in guys:
            ans=find(orders,item)
            if ans:
                mmp[ans]=False
                res.append(ans+1)
            else:
                res.append(-1)
        t-=1
        for item in res:
            print(item,end=" ")
main()
