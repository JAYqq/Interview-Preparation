class Solution:
    def minimumValueAfterDispel(self , nums ):
        self.ans=999999999
        self.dfs(0,nums,0)
        return self.ans
    # def dfs(self,k,nums,index):
    #     t_nums=nums[:]
    #     if k==2:
    #         print(t_nums)
    #         self.ans=min(self.ans,sum(t_nums))
    #         return
    #     t_nums.sort(reverse=True)
    #     for i in range(index,len(t_nums)):
    #         for j in range(i+1):
    #             t_nums[j]-=t_nums[i]
    #         self.dfs(k+1,t_nums,i+1)
so=Solution()
print(so.minimumValueAfterDispel([2, 1, 3]))