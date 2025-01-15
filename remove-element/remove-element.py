class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        
        while s < e :
            if nums[s] == val :
                while nums[e] == val and e > 0:
                    if s >= e :
                        break
                    e -= 1
                
                nums[s], nums[e] = nums[e], nums[s]
             
            s += 1
        
        if e != -1 and nums[e] == val :
            del nums[e:]
        return len(nums)