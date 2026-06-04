class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        max = 0
        for num in nums:
            if num == 1:
                n += 1
                if max < n:
                    max = n
            else:
                n = 0
        return max
