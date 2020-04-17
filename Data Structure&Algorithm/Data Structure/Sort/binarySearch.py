'''本代码是针对力扣33题所写
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/'''
class Solution:
    def mid_search(self,nums:List[int],low:int,high:int,target):
        while high>=low:
            mid=low+((high-low)>>1)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low+=1
            else:
                high-=1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        leng=len(nums)
        max_index=0
        if leng==0:
            return -1
        for i in range(leng):
            if i!=leng-1 and nums[i+1]<nums[i] or i==leng-1:
                max_index=i
                break
        if target>=nums[0]:
            return self.mid_search(nums,0,max_index,target)
        elif target<=nums[leng-1]:
            return self.mid_search(nums,max_index+1,leng-1,target)
        else:
            return -1
        
