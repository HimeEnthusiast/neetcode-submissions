class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1 # Minimum Bananas
        high = max(piles)
        k = 0 # Eating rate
        total_hours = 0 # Time taken to eat all piles at rate of k
        valid_k = []

        while low <= high: # Binary search
            k = low + (high - low) // 2 # Mid

            for pile in piles:
                pile_time = math.ceil(pile / k)
                total_hours += pile_time

            if total_hours <= h and total_hours >= len(piles): # If within range, add to valid array then decrement until you hit min
                valid_k.append(k)
                total_hours = 0
                high = k - 1

            elif total_hours > h:
                total_hours = 0
                low = k + 1

        print(valid_k)
        return min(valid_k)