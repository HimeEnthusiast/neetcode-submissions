class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # nums2 merges into nums1
        # Must be sorted in ascending order
        # m = nums1 elements without nums2
        # n = nums2 elements, amount of 0 placeholoders in nums1
        j = 0

        for i in range(m+n-1, m-1, -1):
            nums1[i] = nums2[j]
            j += 1

        for i in range(1, len(nums1)):    
            while i > 0 and nums1[i] < nums1[i-1]:
                nums1[i], nums1[i-1] = nums1[i-1], nums1[i]
                i -= 1