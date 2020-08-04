import random
class Solution:
    def sub_sort(self,nums,low,high):
        key=nums[low]
        while low<high:
            while low<high and nums[high]>=key:
                high-=1
            while low<high and nums[high]<key:
                nums[low]=nums[high]
                low+=1
                nums[high]=nums[low]
        nums[low]=key
        return low

    def quicksort(self,nums,low,high):
        if low<=high:
            # cur=random.randint(low,high)
            # nums[low],nums[cur]=nums[cur],nums[low]
            key_index=self.sub_sort(nums,low,high)
            if key_index==self.ke:
                return key_index
            elif key_index<self.ke:
                return self.quicksort(nums,key_index+1,high)
            elif key_index>self.ke:
                return self.quicksort(nums,low,key_index)
    def findKthLargest(self, nums, k: int) -> int:
        self.ke=len(nums)-k
        index=self.quicksort(nums,0,len(nums)-1)
        return nums[index]

solution=Solution()
print(solution.findKthLargest([3,3],1))