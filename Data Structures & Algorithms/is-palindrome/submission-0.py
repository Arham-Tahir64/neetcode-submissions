class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        point_l, point_r = 0, len(new) - 1
        while point_l < point_r:
            if new[point_l] != new[point_r]:
                return False
            point_l += 1
            point_r -= 1
        return True

        