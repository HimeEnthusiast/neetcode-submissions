# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        if pairs: 
            states = [pairs.copy()]
        else:
            states = []

        for i in range(1, len(pairs)):
            pair = i

            while pair > 0 and pairs[pair].key < pairs[pair-1].key:
                pairs[pair], pairs[pair - 1] = pairs[pair - 1], pairs[pair]
                pair -= 1

            states.append(pairs.copy())

        return states