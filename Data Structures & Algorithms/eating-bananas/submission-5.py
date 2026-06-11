class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1 # Minimum Bananas
        high = max(piles)
        k = 0 # Eating rate
        valid_k = []

        while low <= high: # Binary search
            total_hours = 0 # Time taken to eat all piles at rate of k
            k = low + (high - low) // 2 # Mid

            for pile in piles: # How long does it take to eat all piles at rate of k 
                pile_time = math.ceil(pile / k)
                total_hours += pile_time

            if total_hours <= h and total_hours >= len(piles): # If within range, add to valid array then decrement until you hit min
                valid_k.append(k)
                high = k - 1

            elif total_hours > h: # If it takes too long, eat faster
                low = k + 1

        return min(valid_k) # Return the smallest k value once all valid k has been found