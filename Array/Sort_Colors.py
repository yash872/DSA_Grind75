# Sort Colors
# https://leetcode.com/problems/sort-colors


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)-1
        l = m = 0
        h = n
        while(m<=h):
            if(nums[m]==0):
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif(nums[m]==1):
                m+=1
            else:
                nums[h],nums[m]=nums[m],nums[h]
                h-=1