class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        comList = []
        for num in heights :
            comList.append(num)
        
        idx = 0
        for i in range(1, len(comList)) :
            if comList[i] < comList[i - 1] :
                idx = i
                while idx > 0 and comList[idx] < comList[idx - 1] :
                    comList[idx], comList[idx - 1] = comList[idx - 1], comList[idx]
                    idx -= 1
        
        count = 0
        for i in range(len(heights)) :
            if heights[i] != comList[i] :
                count += 1
                
        return count
        