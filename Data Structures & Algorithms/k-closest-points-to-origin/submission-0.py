import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [((x*x + y*y), i) for i, (x, y) in enumerate(points)]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            dist, index = heapq.heappop(heap)
            res.append(points[index])
        return res
        