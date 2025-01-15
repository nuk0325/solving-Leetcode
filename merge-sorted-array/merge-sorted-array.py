class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        maxIdx = m - 1
        
        if n != 0 and m != 0 :
            while idx2 < len(nums2) :
                print("idx1:", idx1, "idx2:", idx2)
                if idx1 >= maxIdx and nums1[idx1] == 0 :
                    nums1[idx1] = nums2[idx2]
                    idx2 += 1
                elif nums1[idx1] > nums2[idx2] :
                    nums1.insert(idx1, nums2[idx2])
                    nums1.pop(len(nums1) - 1)
                    idx2 += 1
                    maxIdx += 1
                
                idx1 += 1
        elif m == 0 :
            for num in nums2 :
                nums1[idx1] = num
                idx1 += 1
        
        