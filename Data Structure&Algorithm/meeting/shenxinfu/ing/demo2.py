# class Solution:
#     def min_send(self , nums , m ):
#         self.minn=float('INF')
#         self.nums=nums
#         self.m=m
#         arr=[0]
#         self.dfs(1,arr)
#         return self.minn
#     def dfs(self,time,arr):
#         if time==self.m:
#             return
#         for i in range(arr[-1]+1,len(self.nums)+1):
#             arr.append(i)
#             self.dfs(time+1,arr)
#             arr.append(len(self.nums))
#             # print(arr)
#             maxn=-1
#             for i in range(1,len(arr)):
#                 left=0 if i==1 else arr[i-1]
#                 maxn=max(sum(self.nums[left:arr[i]]),maxn)
#             self.minn=min(maxn,self.minn)
#             arr.pop()
#             arr.pop()

# so=Solution()
# print(so.min_send([4,3,5,10,12],3))
class Solution:
    def min_send(self , nums , m ):
        right=sum(nums)
        res=[]
        left=1
        while left<right:
            mid=(left+right)//2
            ans=0
            time=0
            i=0
            while i<len(nums):
                if ans+nums[i]>mid:
                    ans=0
                    time+=1
                    if time>m:break
                    i-=1
                    # continue
                else:
                    ans+=nums[i]
                i+=1
            if time==m:
                res.append(mid)
                right=mid
            if time>m:
                left=mid+1
            if time<m:
                right=mid
        minn=float('INF')
        for item in res:
            minn=min(item,minn)
        return minn
so=Solution()
print(so.min_send([4,3,5,10,12],2))

