class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        buckets = [[] for _ in range(3)]

        # index = 0
        for n in nums:
            buckets[n].append(n)

        nums[:] = buckets[0] + buckets[1] + buckets[2]
