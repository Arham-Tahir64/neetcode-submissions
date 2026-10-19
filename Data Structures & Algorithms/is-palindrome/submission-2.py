class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(result) - 1


        while l < r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True
        