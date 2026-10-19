class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        out = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for x in range(k):
            out.append(max(freq, key=freq.get))
            del freq[max(freq, key=freq.get)]
        return out


        