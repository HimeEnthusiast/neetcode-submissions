class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = bananas eaten per hour
        # h = hours to eat
        # piles[i] = number of bananas in a pile
        # len(piles) = number of piles
        # math.ceil(piles[i] / k) for each pile
        # use binary search to find minimum k so that hours <= h

        low = 1 # Minimum Bananas
        high = max(piles)
        k = 0 # Eating rate
        total_hours = 0 # Time taken to eat all piles at rate of k
        valid_k = []

        while low <= high:
            k = low + (high - low) // 2
            print(f"Eating rate: {k}")

            for pile in piles:
                pile_time = math.ceil(pile / k)
                print(f"Pile time: {pile_time}")
                total_hours += pile_time

            print(f"Total hours: {total_hours}")

            if total_hours <= h and total_hours >= len(piles): # If within range, add to valid array then decrement until you hit min
                valid_k.append(k)
                total_hours = 0
                high = k - 1

            elif total_hours > h:
                total_hours = 0
                low = k + 1

            else:
                print("All valid rates have been found")
                break

        print(valid_k)
        return min(valid_k)