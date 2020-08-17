class Solution:
    def minimumValueAfterDispel(self , nums ):
        nums.sort(reverse=True)
        maxn=-1
        index=0
        for i in range(len(nums)):
            if nums[i]*(i+1)>=maxn:
                maxn=nums[i]*(i+1)
                index=i
        temp=nums[index]
        for i in range(index+1):
            nums[i]-=temp
        print(nums)
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i]*(i+1)>maxn:
                maxn=nums[i]*(i+1)
                index=i
        temp=nums[index]
        for i in range(i+1):
            nums[i]-=temp
        return sum(nums)
# brr=list(map(int,input().split(" ")))
so=Solution()
print(so.minimumValueAfterDispel([2, 1, 3]))

