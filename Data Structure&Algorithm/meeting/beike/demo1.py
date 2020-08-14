class Solution:
    def reversePairs(self, nums):
        self.copy_nums=[]
        self.ans=0
        self.merge_sort(nums,0,len(nums)-1)
        return self.ans
    def merge_sort(self,nums,left,right):
        if left>=right:return
        mid=left+(right-left)>>1
        self.merge_sort(nums,left,mid)
        self.merge_sort(nums,mid+1,right)
        temp_nums=[]
        i,j=left,mid+1
        while i<=mid and j<=right:
            if nums[i]>nums[j]:
                temp_nums.append(nums[j])
                self.ans+=(mid-i+1)
                j+=1
            else:
                i+=1
                temp_nums.append(nums[i])
        if(i<mid):
            temp_nums.extend(nums[i:mid+1])
        if(j<right):
            temp_nums.extend(nums[j:right+1])
        self.copy_nums=temp_nums
so=Solution()
so.reversePairs([7,5,6,4])