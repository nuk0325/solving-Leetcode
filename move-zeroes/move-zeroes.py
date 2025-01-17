class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(1, len(nums)) :
            if nums[i] != 0 :
                idx = i
                while idx > 0 : 
                    if nums[idx - 1] != 0 :
                        break
                        
                    nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
                    idx -= 1
            