from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        
        l, r = 0, 0
        perm = {}
        while r < len(s2):
            perm[s2[r]] = perm.get(s2[r], 0) + 1
            r += 1

            if r - l > len(s1):
                perm[s2[l]] -= 1
                if perm[s2[l]] == 0:
                    del perm[s2[l]]
                l += 1
            if count == perm:
                return True
        return False

