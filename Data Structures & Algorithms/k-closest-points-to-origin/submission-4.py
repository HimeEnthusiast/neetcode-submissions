class Solution:
    def dist(self, point):
        return point[0]**2 + point[1]**2

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low,high):
            if self.dist(arr[j]) < self.dist(pivot):
                i += 1
                self.swap(arr, i, j)

        self.swap(arr, i + 1, high)
        return i + 1

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort points based off of how close to origin (Smallest coordinates)
        # Return k smallest items in points after Sort (As a list)

        self.quickSort(points, 0, len(points) - 1)

        return points[0:k]