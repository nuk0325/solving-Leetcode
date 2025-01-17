class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        s = 0
        e = len(arr) - 1
        
        if e == 0 :
            return False
        
        while arr[s] < arr[s + 1] and s < e -1 :
            s += 1
        
        while arr[e] < arr[e - 1] and e > 1 :
            e -= 1
            
        if s == 0 or s != e :
            return False
        
        return True
        
        