class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        comList = []
        for num in heights :
            comList.append(num)
        
        hasSwapped = True
        while hasSwapped :
            hasSwapped = False
            for i in range(1, len(comList)) :
                if comList[i] < comList[i - 1] :
                    comList[i], comList[i - 1] = comList[i - 1], comList[i]
                    
                    hasSwapped = True
        
        count = 0
        for i in range(len(heights)) :
            if heights[i] != comList[i] :
                count += 1
        
        return count
        