class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            num = i
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            res[i] = count
        return res

        