import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for n in stones:
            heapq.heappush(max_heap, -n)
        
        while len(max_heap) > 1:
            val1 = (-heapq.heappop(max_heap))
            val2 = (-heapq.heappop(max_heap))
            if val1 > val2:
                heapq.heappush(max_heap, -(val1-val2))
            
        if max_heap:
            return -max_heap[0]
        else:
            return 0