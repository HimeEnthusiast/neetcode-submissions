# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # nums = list(range(1, n + 1))
        
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            pick = guess(mid)

            # Check if x is present at mid
            if pick == 0:
                return mid

            # If x is greater, ignore left half
            elif pick == -1:
                high = mid - 1

            # If x is smaller, ignore right half
            else:
                low = mid + 1

            # If we reach here, then the element
            # was not present
        return n


        