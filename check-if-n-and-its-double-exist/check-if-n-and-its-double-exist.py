class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        for i in range(len(arr)) :
            for j in range(i + 1, len(arr)) :
                print(arr[i], arr[j])
                if arr[i] == 2 * arr[j] or (arr[j] % 2 == 0 and arr[j] / 2 == arr[i]) :
                    return True
        
        return False
                
                