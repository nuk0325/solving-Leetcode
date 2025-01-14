class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for num in nums :
            digit = 1
            
            while num >= 10 :
                num /= 10
                digit += 1
            
            if digit % 2 == 0 :
                count += 1
        
        return count
        