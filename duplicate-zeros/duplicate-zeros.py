class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        idx = 0
        length = len(arr)
        
        while idx < length :
            if arr[idx] == 0 :
                arr.insert(idx + 1, 0)
                arr.pop(length)
                
                idx += 1
            
            idx += 1
