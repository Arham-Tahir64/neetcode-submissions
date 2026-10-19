class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        my_dict2 = {}
        for n in s:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1
        for i in t:
            if i in my_dict2:
                my_dict2[i] += 1
            else:
                my_dict2[i] = 1
        if my_dict == my_dict2:
            return True
        return False
        