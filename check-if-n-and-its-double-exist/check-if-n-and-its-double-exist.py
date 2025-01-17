class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        list = []
        
        for i in range(len(arr)) :
            if arr[i] * 2 in list or (arr[i] % 2 == 0 and arr[i] // 2 in list):
                return True
            
            list.append(arr[i])
        
        return False
                
                